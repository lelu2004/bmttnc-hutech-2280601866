def kiemTraSoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
so = int(input("Nhập một số nguyên: "))
if kiemTraSoNguyenTo(so):
    print("Số " + str(so) + " là số nguyên tố.")
else:
    print("Số " + str(so) + " không phải là số nguyên tố.")