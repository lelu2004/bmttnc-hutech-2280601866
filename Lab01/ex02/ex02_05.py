soGioLam = float(input("Nhập số giờ làm việc trong tuần: "))
luongTheoGio = float(input("Nhập lương theo giờ: "))
gioTieuchuan = 44 # Giờ làm việc tiêu chuẩn trong một tuần
gioVuotChuan = max(0, soGioLam - gioTieuchuan) # Giờ làm việc vượt chuẩn trong tuần
thuc_linh = gioTieuchuan * luongTheoGio + gioVuotChuan * luongTheoGio * 1.5
print("Số tiền thực lĩnh trong tháng là: " + str(thuc_linh))