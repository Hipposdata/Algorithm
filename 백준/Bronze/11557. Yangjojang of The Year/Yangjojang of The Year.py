import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    lst = []
    for j in range(n):
        s, l = sys.stdin.readline().split()
        lst.append((s,int(l)))
    lst.sort(key = lambda x: x[1],reverse = True)
    print(lst[0][0])
