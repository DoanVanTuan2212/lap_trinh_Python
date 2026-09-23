#Hoạt động 1
#Bài tập 1.1
tuoi = 20
if tuoi >= 18:
    print("Da du tuoi")
if tuoi >=18:
    print("Da du tuoi dang ky xe")
else:
    print("Ban chua du tuoi")
#Bài tập 1.2
diem = 7.5

if diem >= 8:
    print("Dat loai gioi")
elif diem >= 6.5:
    print("Dat loai kha")
elif diem >= 5:
    print("Dat loai trung binh")
else:
    print("Dat loai yeu")
#Bài tập 1.3
tuoii = 17
co_giay_phep = False
if tuoii >= 18:
    if co_giay_phep:
        print("Duoc phep lai xe")
    else:
        print("Co giay phep nhung khong du tuoi")
else:
    print("Ban chua du tuoi")
#Bài tập 1.4
diemm = 4.5
ket_qua = "Dat" if diemm >= 5 else "Khong dat"
print(ket_qua)

so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)
#Hoạt động 2
#Bài tập 2.1
ho_ten = "Doan Van T"
diem_toan,diem_ly,diem_hoa = 9.0,8.5,7.5
dtb = round((diem_toan+diem_ly+diem_hoa)/3,2)
if dtb >= 8:
    xep_loai= "Gioi"
elif dtb >= 6.5:
    xep_loai="Kha"
elif dtb >= 5:
    xep_loai="Trung binh"
else:
    xep_loai="Yeu"
print(f"{ho_ten} - DTB: {dtb} - Xep loai: {xep_loai}")    
#Bài tập 2.2
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))
if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c
       
print("So lon nhat la: ", lon_nhat)