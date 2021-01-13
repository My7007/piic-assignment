n = int(input("Nhập n = "))
lst = []
for i in range(n):
    lst.append(int(input()))
tbc_chan = 0
dem1 = 0
tbc_le = 0
dem2 = 0
for t in lst:
    if t % 2 == 0:
     tbc_chan = tbc_chan + t 
     dem1 = dem1 + 1
    else: 
     tbc_le = tbc_le + t
     dem2 = dem2 + 1
print("Trung bình cộng của các số chẵn trong dãy là ", tbc_chan / dem1)
print("Trung bình cộng của các số lẻ trong dãy là ", tbc_le / dem2)