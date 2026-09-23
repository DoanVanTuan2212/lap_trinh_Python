#Hoạt động 5
#Bài tập 5.1
diem = 6.5
if diem >= 8.0:
    pass
elif diem >= 6.5:
    print("Dat yeu cau")
else:
    pass
#Bài tập 5.2
so = 29
la_so_nguyen_to = True
if so <2:
    la_so_nguyen_to=False
else:
    for i in range(2,so):
        if so % i ==0:
            la_so_nguyen_to= False
            break
print(f"{so} co phai la so nguyen to khong? {la_so_nguyen_to}")
#Bài tập 5.3
n = 20
so_hien_tai = n+1
while True:
    la_so_nguyen_to= True
    for i in range(2,so_hien_tai):
        if so_hien_tai%i==0:
            la_so_nguyen_to=False
            break
    if la_so_nguyen_to:
        break
    so_hien_tai +=1
print(f"so nguyen to dau tien lon hon {n} la {so_hien_tai}")
#Bài tập 5.4
danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []
for so1 in danh_sach:
    if so1 <=0:
        continue
    danh_sach_hop_le.append(so1)
print("cac so hop le(duong): ", danh_sach_hop_le)
#Hoạt động 6
#Bài tập 6.1
l = 5
for i in range(1,l +1):
    for j in range(i):
        print("*",end="")
    print()
#Bài tập 6.2
c = 4
for i in range(i, c +1):
    print(" "* (n-1) + "*" *(2*i-1))
for i in range(c -1,0,-1):
    print(" " * (n - i) + "*" * (2 * i - 1))