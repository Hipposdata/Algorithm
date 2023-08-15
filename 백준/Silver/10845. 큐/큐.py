import sys
from collections import deque

n = int(input())
q = deque([])
dap = []

for i in range(n):
    ipreak = sys.stdin.readline().split()
    if ipreak[0] == "push":
        q.append(ipreak[1])
    elif ipreak[0] == "pop":
        if len(q)== 0:
            dap.append(-1)
        else:
            dap.append(q.popleft()) ###
    elif ipreak[0] == "size":
        dap.append(len(q))
    elif ipreak[0] == "empty":
        if len(q) == 0:
            dap.append(1)
        else:
            dap.append(0)
    elif ipreak[0] == "front":
        if len(q) == 0:
            dap.append(-1)
        else:
            dap.append(q[0])
    elif ipreak[0] == "back":
        if len(q) == 0:
            dap.append(-1)
        else:
            dap.append(q[-1])

dap = map(int,dap)
for i in dap:
    print(i)
