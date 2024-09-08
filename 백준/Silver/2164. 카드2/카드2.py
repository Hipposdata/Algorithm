import sys
from collections import deque
n = int(sys.stdin.readline())

lst = deque(i for i in range(n,1-1,-1))

while len(lst) >1:
    lst.pop()
    lst.appendleft(lst[-1])
    lst.pop()
print(lst[0])
