from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while True:
    print("----- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN -----")
    print("1. Thêm sinh viên")
    print("2. Cập nhật sinh viên")
    print("3. Hiển thị danh sách sinh viên")
    print("4. Sắp xếp sinh viên theo ID")
    print("5. Tìm kiếm sinh viên theo tên")
    print("6. Xóa sinh viên theo ID")
    print("7. Thoát")
    
    choice = input("Chọn chức năng (1-7): ")
    
    if (choice == '1'):
        qlsv.nhap_sinh_vien()
        
    elif (choice == '2'):
        try:
            ma_sv = int(input("Nhập mã số sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(ma_sv)
        except ValueError:
            print("Mã sinh viên phải là số!")

    elif (choice == '3'):
        # Sử dụng hàm showSinhVien có sẵn thay vì viết lại vòng lặp print
        qlsv.showSinhVien(qlsv.list_sinh_vien)

    elif (choice == '4'):
        qlsv.sortByID()
        print("\n-> Danh sách sinh viên đã được sắp xếp theo ID.")
        qlsv.showSinhVien(qlsv.list_sinh_vien)

    elif (choice == '5'):
        name = input("Nhập tên sinh viên cần tìm kiếm: ")
        ketqua = qlsv.findByName(name)
        print(f"\n-> Tìm thấy {len(ketqua)} sinh viên:")
        qlsv.showSinhVien(ketqua)

    elif (choice == '6'):
        try:
            ma_sv = int(input("Nhập mã số sinh viên cần xóa: "))
            isdeleted = qlsv.deleteByID(ma_sv)
            if isdeleted:
                print("-> Xóa sinh viên thành công.")
            else:
                print("-> Không tìm thấy sinh viên với mã số đã cho.")
        except ValueError:
            print("Mã sinh viên phải là số!")

    elif (choice == '7'):
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")