
import sys
N = int(sys.stdin.readline() )
lst = []
for _ in range(N):
    tmp =int(sys.stdin.readline() )
    lst.append(tmp)

lst.sort()
for i in range(N):
    print(lst[i])