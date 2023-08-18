import sys
from collections import deque
n = int(sys.stdin.readline())
d = deque([])
dap = []

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push_front":
        d.appendleft(a[1])
    elif a[0] == "push_back":
        d.append(a[1])
    elif a[0] == "pop_front":
        if len(d) == 0:
            dap.append(-1)
        else:
            # d.popleft()
            dap.append(d.popleft()) #########
            # d.popleft()
    elif a[0] == "pop_back":
        if len(d) == 0:
            dap.append(-1)
        else:
            dap.append(d.pop()) #########
            # d.pop()
    elif a[0] == "size":
        dap.append(len(d))
    elif a[0] == "empty":
        if len(d) == 0:
            dap.append(1)
        else:
            dap.append(0)
    elif a[0] == "front":
        if len(d) == 0:
            dap.append(-1)
        else:
            dap.append(d[0])
    elif a[0] == "back":
        if len(d) == 0:
            dap.append(-1)
        else:
            dap.append(d[-1])

dap =  map(int,dap)
for i in dap:
    print(i)

