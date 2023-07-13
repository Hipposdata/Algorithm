lst = []
hap = 0
for i in range(5):
    a = int(input())
    lst.append(a)
    hap += a
lst.sort()
print(int(hap/5))
print(lst[2])