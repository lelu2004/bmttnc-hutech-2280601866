print("Nhập các dòng văn bản(Nhập 'done' để kết thúc):")
lines =[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("Các dòng đã nhập sau khi chuyển thành chữ in hoa là:")
for l in lines:
    print(l.upper())