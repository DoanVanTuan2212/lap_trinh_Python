ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))
#Yêu cầu: giải thích vì sao phải ép kiểu int()/float() cho nam_sinh và diem_tb, trong khi ho_ten thì không
#ho_ten: là chuỗi ký tự (str) nên dữ liệu nhập vào từ input() đã đúng kiểu cần dùng → không cần ép kiểu.
#nam_sinh: cần thực hiện các phép tính hoặc so sánh với số → phải chuyển từ chuỗi sang số nguyên bằng int().
#diem_tb: có thể chứa số thập phân (ví dụ 8.5) → phải chuyển sang số thực bằng float().

print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")
print("Dong 1", end=" | ")
print("Dong 2")
#Yêu cầu: thử đổi sep thành nhiều ký tự khác nhau (", ", "\n") và quan sát kết quả rồi giải thích.
#sau khi đổi các kí tự thì giữa các từ sẽ thay đổi theo như ví dụ \n thì giữa các từ sẽ xuống dòng

# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
# toán tử %

print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))
#Vì f-string ngắn gọn, dễ đọc và dễ viết hơn khi chèn biến vào chuỗi.

#Hoạt động 2
# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Tran Thi B" # bien luu ho ten
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
#s4 dùng chuỗi bình thường: C:\\Python\\data. Trong chuỗi thường, \\ được hiểu là một dấu \. Vì vậy khi in ra sẽ là C:\Python\data.
#s5 dùng raw string với tiền tố r: r"C:\Python\data". Raw string giữ nguyên các dấu \, không xử lý chúng như ký tự escape thông thường.
#Raw string thường dùng khi:
#Viết đường dẫn Windows: r"C:\Python\data"
#Viết biểu thức chính quy (regex), vì regex sử dụng rất nhiều dấu \
