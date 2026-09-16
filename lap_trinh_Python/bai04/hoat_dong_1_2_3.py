#Hoạt động 1
#Bài tập 1.1
sinh_vien={"ho_ten":"Doan Van Tuan","nam_sinh":2006,"diem":8.5}
print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem"))
print(sinh_vien.get("lop","Chua co"))
#
#Bài tập 1.2
sinh_vien["lop"]="CNTT01"
sinh_vien["diem_TB"]= 9.0
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_TB")
print(sinh_vien,"- diem da xoa:",diem_cu)
sinh_vien.update({"nam_sinh":2005,"email":"dvidtuan06@gmail.com"})
print(sinh_vien)
#Hoạt động 2
diem_mon_hoc = {"Toan":8.0,"Ly":7.5,"Hoa":9.5,"Van":9.0}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)
for mon,diem in diem_mon_hoc.items():
    print(f"{mon}:{diem}")
tong_diem=0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("Diem trung binh:",round(tong_diem/len(diem_mon_hoc),2))
#Hoạt động 3
#Bài tập 3.1
diem_cong_diem = {mon:round(diem+0.5,2) for mon,diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon,diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)
#Bài tập 3.2
mon_hoc_ky1 = {"Toan","Ly","Hoa","Van"}
mon_hoc_ky2 = {"Toan","Anh","Tin","Van"}
print(mon_hoc_ky1 & mon_hoc_ky2)
print(mon_hoc_ky1| mon_hoc_ky2)
print(mon_hoc_ky1 - mon_hoc_ky2)
#