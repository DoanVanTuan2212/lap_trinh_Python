#Hoạt động 1
#Bài tập 1.1
def uscln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def bcsnn(a,b):
    return a*b// uscln(a,b)
def kiem_tre_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    return tong_uoc==n
print(uscln(24,36))
print(bcsnn(4,6))
print(kiem_tre_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28))
#Bài tập 1.2
def in_loi_chao(ten):
    print(f"Xin chao {ten}")
    return
def chia_lay_phan_du(a,b):
    return a//b,a%b
in_loi_chao("An")
thuong,du = chia_lay_phan_du(30,16)
print(f"Thuong: {thuong} Du:{du}")
#Hoạt động 2
def gioi_thieu(ten , tuoi =18,lop="Chua ro"):
    print(f"Ten :{ten}-Tuoi:{tuoi}_Lop:{lop}")
gioi_thieu("An")
gioi_thieu("Binh", 20) 
gioi_thieu("Chi", lop="CNTT01")
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)
#Khi gọi hàm bằng tham số từ khóa (ten=..., lop=..., tuoi=...), thứ tự truyền vào không quan trọng vì
# Python xác định giá trị dựa vào tên của tham số, chứ không dựa vào vị trí.
#Hoạt động 3
#bài tập 3.1
def tinh_tong(*args):
    tong =0
    for so in args:
        tong+=so
    return tong
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())
#bài tập 3.2
def in_thong_tin(ho_ten,tuoi,**kwargs):
    print(f"Ho ten: {ho_ten} tuoi: {tuoi}")
    for khoa,gia_tri in kwargs.items():
        print(f"{khoa} {gia_tri}")
in_thong_tin("Doan Van Tuan",20,lop="CNTT",que_quan="Hai Phong")
in_thong_tin("Tran Thi B",21,email="b@gmail.com")
