def dem_so_lan_xuat_hien(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count 
input_string = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ")
word_list = input_string.split()

dem_so_lan_xuat_hiens = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của mỗi phần tử trong danh sách là:", dem_so_lan_xuat_hiens)