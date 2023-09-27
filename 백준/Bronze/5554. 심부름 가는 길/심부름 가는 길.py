import sys

lst = []

for i in range(4):
    num = int(sys.stdin.readline())
    lst.append(num)

hap = sum(lst)
print(hap//60)
print(hap%60)