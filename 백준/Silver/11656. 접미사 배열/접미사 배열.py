import sys

s = sys.stdin.readline().strip()
lst = []
for i in range(len(s)):
    tmp = s[i:]
    lst.append(tmp)

lst.sort()
for j in lst:
    print(j)