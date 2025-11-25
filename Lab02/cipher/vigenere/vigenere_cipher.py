class VigenereCipher:
    def __init__(self):
        pass 
        
    def encrypt_text(self, plain_text, key): 
        encrypted_text = []
        key_index = 0
        
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                
                if char.isupper():
                    base = ord('A')
                    encrypted_char = chr((ord(char) - base + key_shift) % 26 + base)
                else:
                    base = ord('a')
                    encrypted_char = chr((ord(char) - base + key_shift) % 26 + base)
                    
                encrypted_text.append(encrypted_char) 
                key_index += 1
            else:
                encrypted_text.append(char)
        return "".join(encrypted_text) 

    def decrypt_text(self, cipher_text, key): 
        decrypted_text = []
        key_index = 0
        
        for char in cipher_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                
                if char.isupper():
                    base = ord('A')
                    decrypted_char = chr((ord(char) - base - key_shift) % 26 + base)
                else:
                    base = ord('a')
                    decrypted_char = chr((ord(char) - base - key_shift) % 26 + base)
                    
                decrypted_text.append(decrypted_char)
                key_index += 1
            else:
                decrypted_text.append(char)

        return "".join(decrypted_text)