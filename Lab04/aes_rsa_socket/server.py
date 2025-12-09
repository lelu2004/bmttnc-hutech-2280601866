from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

# Cấu hình Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server is listening on port 12345...")

# Server key (Dùng để trao đổi ban đầu nếu cần, ở logic này chủ yếu dùng key của client)
server_key = RSA.generate(2048)

clients = [] # Lưu trữ tuple (socket, aes_key)

def encrypt_message(aes_key, message):
    cipher = AES.new(aes_key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(aes_key, encrypted_data):
    try:
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data.decode()
    except Exception as e:
        return None

def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")
    
    try:
        # 1. Gửi Public Key của Server (Tuỳ chọn, code gốc của bạn có gửi)
        client_socket.send(server_key.public_key().export_key(format='PEM'))
        
        # 2. Nhận Public Key của Client
        client_received_key_data = client_socket.recv(2048)
        client_public_key = RSA.import_key(client_received_key_data)
        
        # 3. Tạo AES Key ngẫu nhiên cho session này
        aes_key = get_random_bytes(16)
        
        # 4. Mã hoá AES Key bằng RSA Public Key của Client và gửi lại
        cipher_rsa = PKCS1_OAEP.new(client_public_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        client_socket.send(encrypted_aes_key)
        
        # Lưu client vào danh sách
        clients.append((client_socket, aes_key))

        while True:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break
            
            # Giải mã tin nhắn từ client gửi lên
            msg_content = decrypt_message(aes_key, encrypted_msg)
            
            if msg_content:
                print(f"Received from {client_address}: {msg_content}")
                
                if msg_content == "exit":
                    break

                # Broadcast: Gửi cho các client khác
                # LƯU Ý: Phải mã hoá lại bằng AES Key riêng của từng client đích
                for client, k in clients:
                    if client != client_socket:
                        try:
                            msg_to_send = encrypt_message(k, msg_content)
                            client.send(msg_to_send)
                        except:
                            pass # Xử lý lỗi nếu client bị ngắt kết nối đột ngột
            else:
                break

    except Exception as e:
        print(f"Error with {client_address}: {e}")
    finally:
        # Dọn dẹp kết nối
        print(f"Connection with {client_address} closed")
        if (client_socket, aes_key) in clients:
            clients.remove((client_socket, aes_key))
        client_socket.close()

# Vòng lặp chính để chấp nhận kết nối (Phải nằm ngoài handle_client)
while True:
    client_sock, client_addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
    client_thread.start()