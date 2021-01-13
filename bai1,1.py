n = int(input("Nhập n = "))
list1 = []
for i in range(n):
    list1.append(int(input()))
tong = 0
for t in list1:
    tong = tong + t 
print(tong)