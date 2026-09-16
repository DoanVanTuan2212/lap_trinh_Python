quan_ly_diem = {
    "Tran Thi A":[8.5,7.0,9.4],
    "Doan Van T":[7.1,5.7,8.8],
    "Pham Thai C":[5.1,6.3,7.2]
}
quan_ly_diem["Vu Thi M"]=[5.5,7.7,3.3]
quan_ly_diem["Doan Van T"][0] = 9.0
diem_trung_binh={}
for ho_ten,danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(sum(danh_sach_diem)/len(danh_sach_diem),2)
print("BANG DIEM TRUNG BINH")
for ho_ten,dtb in diem_trung_binh.items():
    dat_loai_gioi = dtb >= 8.0
    print(f"{ho_ten:<15} - DTB: {dtb:<6} - Dat loai gioi? {dat_loai_gioi}")