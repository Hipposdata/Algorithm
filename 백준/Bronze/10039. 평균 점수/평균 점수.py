import sys

lst = []

for i in range(5):
    num = int(sys.stdin.readline())
    if num <40:
        lst.append(40)
    else:
        lst.append(num)

print(sum(lst)//5)
