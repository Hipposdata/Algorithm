import sys
lst = []
t = int(sys.stdin.readline())
for i in range(t):
    n = list(sys.stdin.readline())[:-1]
    lst.append(n)
res = lst[0]
for i in range(len(lst)-1):
    for j in range(0,len(res)):
        if lst[i][j] != lst[i+1][j]:
            res[j] = '?'

print("".join(res))