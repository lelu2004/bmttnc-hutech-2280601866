def chia_het_cho_5(soNhiPhan):
    soThapPhan = int(soNhiPhan, 2)
    if soThapPhan % 5 == 0:
        return True
    else:
        return False
chuoiNhiPhan = input("Nhập một số nhị phân(Phân tách bởi dấu phẩy): ")
soNhiPhanList = chuoiNhiPhan.split(',')
soNhiPhanChiaHet5 = [so for so in soNhiPhanList if chia_het_cho_5(so)]
if len(soNhiPhanChiaHet5) > 0:
        ketqua = ', '.join(soNhiPhanChiaHet5)
        print("Các số nhị phân chia hết cho 5 là: ", ketqua)
else:
        print("Không có số nhị phân nào chia hết cho 5.")