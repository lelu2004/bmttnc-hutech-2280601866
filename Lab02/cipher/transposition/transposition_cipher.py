class TranspositionCipher:
    def __init__(self):
        pass
    def encrypt(self, plain_text, key):
        encrypted_text = ''
        for i in range(key):
            pointer = i
            while pointer < len(plain_text):
                encrypted_text += plain_text[pointer]
                pointer += key
        return encrypted_text
    def decrypt(self, cipher_text, key):
        decrypt_text = [''] * key
        row, col = 0, 0
        for i in cipher_text:
            decrypt_text[col] += i
            col += 1
            if (col == key) or (col == key - 1 and row >= len(cipher_text) % key):
                row += 1
                col = 0
        return ''.join(decrypt_text)