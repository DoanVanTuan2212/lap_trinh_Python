#Bài tập 6.1
def giai_thua_de_quy(n):
 if n <= 1: 
   return 1
 return n * giai_thua_de_quy(n - 1)
def giai_thua_lap(n):
 ket_qua = 1
 for i in range(1, n + 1):
  ket_qua *= i
 return ket_qua
print(giai_thua_de_quy(5), "-", giai_thua_lap(5))
#Cả đệ quy và vòng lặp đều có thể dùng để tính giai thừa và cho cùng kết quả.
# Đệ quy sử dụng hàm tự gọi lại chính nó và cần có điều kiện dừng. 
# Vòng lặp sử dụng for để thực hiện phép nhân tuần tự.
#Bài tập 6.2
def fibonacci_de_quy(n):
  if n <= 1: 
   return n
  return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
for i in range(10):
  print(fibonacci_de_quy(i), end=" ")
print()
#Đệ quy Fibonacci tốn kém hơn đệ quy giai thừa vì mỗi lần gọi fibonacci_de_quy(n) lại
#tạo ra hai lời gọi fibonacci_de_quy(n-1) và fibonacci_de_quy(n-2)
