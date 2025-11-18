def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập danh sách số nguyên, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tuple_ket_qua = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple: ", tuple_ket_qua)