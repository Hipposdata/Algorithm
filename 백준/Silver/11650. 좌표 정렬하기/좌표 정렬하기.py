import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    a = (x,y)
    lst.append(a)
lst.sort()

for i in range(N):
    lst[i] = list(map(str,lst[i]))
    print(' '.join(lst[i]))