danh_sach_sinh_vien = [
    {"ma_sv": "SV001", "ho_ten": "Nguyen Van An", "tuoi": 20, "lop": "CNTT01", "diem_tb": 8.5},
    {"ma_sv": "SV002", "ho_ten": "Tran Thi Binh", "tuoi": 19, "lop": "CNTT01", "diem_tb": 7.8},
    {"ma_sv": "SV003", "ho_ten": "Le Van Cuong", "tuoi": 21, "lop": "CNTT02", "diem_tb": 9.0},
    {"ma_sv": "SV004", "ho_ten": "Pham Thi Dung", "tuoi": 20, "lop": "CNTT02", "diem_tb": 8.2},
]

lich_su_diem = []
def hien_thi_danh_sach_sinh_vien():
    print("\n" + "=" * 75)
    print(f"{'Ma SV':<10}{'Ho ten':<20}{'Tuoi':<8}{'Lop':<12}{'Diem TB':<10}")
    print("-" * 75)

    for sinh_vien in danh_sach_sinh_vien:
        print(f"{sinh_vien['ma_sv']:<10}"
              f"{sinh_vien['ho_ten']:<20}"
              f"{sinh_vien['tuoi']:<8}"
              f"{sinh_vien['lop']:<12}"
              f"{sinh_vien['diem_tb']:<10.2f}")

    print("=" * 75)


def tim_sinh_vien_theo_ma(ma_sv):
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien["ma_sv"] == ma_sv:
            return sinh_vien
    return None


def xem_sinh_vien_gioi():
    sinh_vien_gioi = [
        sinh_vien for sinh_vien in danh_sach_sinh_vien
        if sinh_vien["diem_tb"] >= 8.0
    ]

    if len(sinh_vien_gioi) == 0:
        print("-> Hien khong co sinh vien nao dat diem TB tu 8.0 tro len.")
        return

    print("\nCAC SINH VIEN CO DIEM TB >= 8.0:")

    for sinh_vien in sinh_vien_gioi:
        print(f" {sinh_vien['ma_sv']} - "
              f"{sinh_vien['ho_ten']} - "
              f"{sinh_vien['lop']} - "
              f"{sinh_vien['diem_tb']:.2f}")
def them_sinh_vien(ma_sv, ho_ten, tuoi, lop, diem_tb):
    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return

    danh_sach_sinh_vien.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "lop": lop,
        "diem_tb": diem_tb
    })

    print(f"-> Da them sinh vien {ma_sv} thanh cong.")


def cap_nhat_diem(ma_sv, diem_moi):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    sinh_vien["diem_tb"] = diem_moi

    print(f"-> Da cap nhat diem sinh vien {ma_sv} thanh cong.")


def xoa_sinh_vien(ma_sv):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    danh_sach_sinh_vien.remove(sinh_vien)

    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")
def thong_ke_diem():
    if len(lich_su_diem) == 0:
        print("-> Chua co lich su cap nhat diem nao.")
        return

    print("\nLICH SU CAP NHAT DIEM:")

    for gd in lich_su_diem:
        print(f" {gd['ma_sv']} - {gd['ho_ten']} - "
              f"Diem cu: {gd['diem_cu']:.2f} - "
              f"Diem moi: {gd['diem_moi']:.2f}")


def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")
def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach tat ca sinh vien")
    print("2. Xem sinh vien gioi")
    print("3. Them sinh vien moi")
    print("4. Cap nhat diem sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke diem")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_sinh_vien()

        elif lua_chon == "2":
            xem_sinh_vien_gioi()

        elif lua_chon == "3":
            ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()
            ho_ten = input("Nhap ho ten sinh vien: ").strip().title()
            tuoi = nhap_so_nguyen("Nhap tuoi: ")
            lop = input("Nhap lop: ").strip().upper()
            diem_tb = float(input("Nhap diem trung binh: "))

            them_sinh_vien(ma_sv, ho_ten, tuoi, lop, diem_tb)

        elif lua_chon == "4":
            ma_sv = input("Nhap ma sinh vien can cap nhat diem: ").strip().upper()
            diem_moi = float(input("Nhap diem moi: "))

            cap_nhat_diem(ma_sv, diem_moi)

        elif lua_chon == "5":
            ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()

            xoa_sinh_vien(ma_sv)

        elif lua_chon == "6":
            thong_ke_diem()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()