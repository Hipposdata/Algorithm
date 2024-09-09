# 버블 정렬

import sys
n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))


for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for k in lst:
    print(k)
