import base64

def main():
    try:
        input_string = input("Nhập thông tin cần mã hóa: ")
        encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
        encoded_string = encoded_bytes.decode("utf-8")
        
        with open("data.txt", "w") as file:
            file.write(encoded_string)
            
        print("Đã mã hóa và ghi vào tệp data.txt")
        
    except Exception as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    main()