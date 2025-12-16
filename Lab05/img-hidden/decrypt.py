import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                # Lấy bit cuối cùng
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    # Gom mỗi 8 bit thành 1 ký tự
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8: break 
        
        # Kiểm tra dấu hiệu kết thúc (trong encrypt dùng 1111111111111110, ở đây check ký tự null hoặc EOF tùy logic)
        # Theo code mẫu trong Lab:
        char = chr(int(byte, 2))
        
        # Lưu ý: Code gốc trong ảnh có đoạn check char == '\0', 
        # nhưng encrypt lại đánh dấu bằng chuỗi bit 1. 
        # Để code chạy đúng với encrypt phía trên, ta nên check chuỗi bit đánh dấu.
        # Tuy nhiên, dưới đây là code bám sát theo tài liệu:
        if char == '\0': 
             break
             
        # Cập nhật logic để dừng nếu gặp dấu hiệu kết thúc thực tế từ encrypt (2 byte 255, 254)
        if i + 16 <= len(binary_message):
             if binary_message[i:i+16] == '1111111111111110':
                 break

        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()