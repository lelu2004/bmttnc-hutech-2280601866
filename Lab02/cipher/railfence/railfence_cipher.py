class RailFenceCipher:
    def __init__(self):
        pass 
    
    def encrypt_text(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text
        rails = [[] for _ in range(num_rails)]
        rail = 0
        direction = 1
        
        for char in plain_text:
            rails[rail].append(char)
            if rail == 0:
                direction = 1
            elif rail == num_rails - 1:
                direction = -1
            rail += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def decrypt_text(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text
        rail_lengths = [0] * num_rails
        rail = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            rail_lengths[rail] += 1
            if rail == 0:
                direction = 1
            elif rail == num_rails - 1:
                direction = -1
            rail += direction
  
        rails = []
        index = 0
        for length in rail_lengths:
            rails.append(cipher_text[index:index + length])
            index += length
            
        plaintext = ""  
        rail_indices = [0] * num_rails
        rail = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            plaintext += rails[rail][0]
            rails[rail] = rails[rail][1:]
            if rail == 0:
                direction = 1
            elif rail == num_rails - 1:
                direction = -1
            rail += direction
        return plaintext