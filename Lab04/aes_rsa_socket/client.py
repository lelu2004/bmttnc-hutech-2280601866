from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Tạo RSA key cho client
client_key = RSA.generate(2048)

# 1. Nhận Server Public Key (nhận nhưng chưa dùng trong logic này, để cho khớp với server)
server_public_key = RSA.import_key(client_socket.recv(2048))

# 2. Gửi Client Public Key lên Server
client_socket.send(client_key.public_key().export_key(format='PEM'))

# 3. Nhận AES Key đã mã hoá từ Server
encrypted_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

print("Connected via secure AES channel.")

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message_func(key, encrypted_data):
    try:
        # Sửa lỗi logic slicing ở đây: [AES.block_size:] thay vì [AES.block_size]
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data.decode()
    except Exception as e:
        return "Error decrypting message"

def receive_message():
    while True:
        try:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break
            # Đổi tên hàm decrypt để tránh trùng lặp
            msg = decrypt_message_func(aes_key, encrypted_msg)
            print(f"\nBroadcast: {msg}\nEnter message ('exit' to quit): ", end="")
        except:
            print("Connection closed.")
            break

# Chạy luồng nhận tin nhắn
receive_thread = threading.Thread(target=receive_message)
receive_thread.daemon = True # Tự động tắt khi chương trình chính tắt
receive_thread.start()

while True:
    message = input("Enter message ('exit' to quit): ")
    if message == 'exit':
        encrypted_msg = encrypt_message(aes_key, message)
        client_socket.send(encrypted_msg)
        break
    
    encrypted_msg = encrypt_message(aes_key, message)
    client_socket.send(encrypted_msg)

client_socket.close()