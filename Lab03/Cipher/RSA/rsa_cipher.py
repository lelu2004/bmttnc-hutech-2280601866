from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5 
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5 
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self):
        if not os.path.exists('Cipher/RSA/keys'):
            os.makedirs('Cipher/RSA/keys', exist_ok=True)

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        with open('Cipher/RSA/keys/private.pem', 'wb') as f:
            f.write(private_key)
        with open('Cipher/RSA/keys/public.pem', 'wb') as f:
            f.write(public_key)

    def load_keys(self):
        try:
            with open('Cipher/RSA/keys/private.pem', 'rb') as f:
                private_key = f.read()
            with open('Cipher/RSA/keys/public.pem', 'rb') as f:
                public_key = f.read()
            return private_key, public_key
        except FileNotFoundError:
            self.generate_keys()
            return self.load_keys()

    def encrypt(self, message, key):
        rsa_key = RSA.importKey(key)
        cipher = Cipher_PKCS1_v1_5.new(rsa_key) 
        ciphertext = cipher.encrypt(message.encode('utf-8'))
        return ciphertext

    def decrypt(self, ciphertext, key):
        rsa_key = RSA.importKey(key)
        cipher = Cipher_PKCS1_v1_5.new(rsa_key) 
        sentinel = b"Error decoding"
        decrypted_message = cipher.decrypt(ciphertext, sentinel)
        return decrypted_message.decode('utf-8')

    def sign(self, message, key):
        rsa_key = RSA.importKey(key)
        signer = Signature_PKCS1_v1_5.new(rsa_key) 
        digest = SHA256.new(message.encode('utf-8'))
        signature = signer.sign(digest)
        return signature

    def verify(self, message, signature, key):
        rsa_key = RSA.importKey(key)
        verifier = Signature_PKCS1_v1_5.new(rsa_key) # Dùng Signature (Đã sửa)
        digest = SHA256.new(message.encode('utf-8'))
        try:
            verifier.verify(digest, signature)
            return True
        except (ValueError, TypeError):
            return False