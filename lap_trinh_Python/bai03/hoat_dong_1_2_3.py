#Bài tập 1.1
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0])
print(diem_so[-1])
print(diem_so[1:4])
print(diem_so[::2])
print(diem_so[::-1])
#Bài tập 1.2
Ten_sv = ["An","Chi","Binh"]
Ten_sv.append("Dung")
Ten_sv.insert(1,"Tuan")
print(Ten_sv)
Ten_sv.remove("Chi")
pop_ra=Ten_sv.pop()
print(Ten_sv, "- da xoa:", pop_ra)
Ten_sv.sort()
print(Ten_sv)
Ten_sv.reverse()
print(Ten_sv)
Ten_sv.extend(["Duong","Khanh"])
print(Ten_sv)
#Trả lời câu hỏi:remove() là xóa giá trị theo chỉ định ví dụ muốn xóa Chi thì khi in ra list sẽ không còn Chi
#còn pop() là xóa phần tử cuối
#HOẠT ĐỘNG 2
#Bài tập 2.1
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
    tong += tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))
#Bài tập 2.2
ma_tran = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# In ra theo tung hang
for hang in ma_tran:
    print(hang)
# In ra tung phan tu, duyet theo hang roi theo cot
for hang in ma_tran:
 for phan_tu in hang:
  print(phan_tu, end=" ")
print()
tong = 0

for hang in ma_tran:
    for phan_tu in hang:
        tong += phan_tu

print("Tổng các phần tử =", tong)
#Hoạt động 3
#Bài tập 3.1
day_so = list(range(1, 21)) 
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("So chan:", so_chan)
print("So le:", so_le)
#Bài tập 3.2
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print(diem_cong)