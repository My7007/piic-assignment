n = int(input("Nhập n ="))
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst)
t = int(input("Vị trí cần xóa là:"))
lst.pop(t)
print(lst)