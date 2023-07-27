########################  오세푸스 ###########
import sys
N, K = map(int,sys.stdin.readline().split())
from collections import deque
lst = deque()
for i in range(1,N+1):
    lst.append(i)
dap = []
while len(lst) >= 2:
    for i in range(K-1):
        lst.append(lst[0])
        lst.popleft()
    dap.append(lst[0])
    lst.popleft()
dap.append(lst[0])

dap1 = ''
for i in dap:
    if i ==dap[-1]:
        dap1 += str(i)
    else:
        dap1 += str(i)+ ', '
print('<'+dap1+'>')