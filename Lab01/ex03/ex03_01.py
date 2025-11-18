def tinh_tong_so_chan(n):
    tong = 0
    for num in n:
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhập danh sách số nguyên, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
result = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:", result)