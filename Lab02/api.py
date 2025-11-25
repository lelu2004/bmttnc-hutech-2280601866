from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher # Import class Vigenere

app = Flask(__name__)

# --- KHỞI TẠO CÁC ĐỐI TƯỢNG MÃ HÓA ---
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()

# ================= CAESAR =================
@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    # Gọi hàm encrypt_text từ class Caesar
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    # Gọi hàm decrypt_text từ class Caesar
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# ================= VIGENERE =================
@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key'] 
    
    # SỬA: Gọi hàm encrypt_text (tên mới) và bỏ .join()
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    
    # SỬA: Gọi hàm decrypt_text (tên mới) và bỏ .join()
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    
    return jsonify({'decrypted_text': decrypted_text})

# ================= MAIN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)