import sys
from collections import deque

def command(n):
    if n[0] == 1:
        d.appendleft(n[1])
    elif n[0] == 2:
        d.append(n[1])
    elif n[0] == 3:
        if len(d) == 0:
            dap.append(-1)
        else:
            dap.append(d.popleft())
    elif n[0] == 4:
        if len(d) == 0:
            dap.append(-1)
        else:
            dap.append(d.pop())
    elif n[0] == 5:
        dap.append(len(d))
    elif n[0] == 6:
        if len(d) == 0:
            dap.append(1)
        else:
            dap.append(0)
    elif n[0] == 7:
        if len(d) == 0:
            dap.append(-1)
        else:
            dap.append(d[0])
    elif n[0] == 8:
        if len(d) ==0:
            dap.append(-1)
        else:
            dap.append(d[-1])

d = deque()
N = int(sys.stdin.readline())
dap = []
for i in range(N):
    n = list(map(int,sys.stdin.readline().split()))
    command(n)

for i in dap:
    print(i)