import sys
from collections import deque
lst = deque()
N = int(input())
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        lst.append(cmd[1])
    if cmd[0] == 'pop':
        if len(lst) >=1:
            print(lst[0])
            lst.popleft()
        else:
            print(-1)
    if cmd[0] == 'size':
        print(len(lst))
    if cmd[0] == 'empty':
        if len(lst) >= 1:
            print(0)
        else:
            print(1)
    if cmd[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    if cmd[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])