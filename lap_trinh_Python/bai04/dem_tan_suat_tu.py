doan_van = "python la ngon ngu lap trinh python de hoc python de thuc hanh"
danh_sach_tu=doan_van.split()
tan_suat={}
for tu in danh_sach_tu:
    tan_suat[tu]=tan_suat.get(tu,0)+1
print("tan suat xuat hien cac ty:")
for tu,so_lan in tan_suat.items():
    print(f"{tu}:{so_lan}")
#tan_suat.get(tu, 0) + 1 giúp kiểm tra và đếm từ trong một dòng.
# Nếu tu đã tồn tại trong Dictionary, get() lấy số lần xuất hiện hiện tại;
# nếu chưa tồn tại, get() trả về 0. Sau đó + 1 để tăng số lần xuất hiện lên một.