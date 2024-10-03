import sys
from collections import deque

n,w,l = map(int,sys.stdin.readline().split())
dq_before = deque(map(int,sys.stdin.readline().split()))

dq_bridge = deque([0] * w) # 최대 다리 길이 w

dap = 0
while True:
    if not dq_before and sum(dq_bridge) == 0:
        break
    if not dq_before: # dq_before 비어있다면
        dq_bridge.popleft()
        dq_bridge.append(0)
        dap +=1
    else: # dq_before 비어있지않다면
        if dq_before[0] + sum(dq_bridge) - dq_bridge[0] <= l:
            dq_bridge.popleft()
            dq_bridge.append(dq_before[0])
            dq_before.popleft()
            dap +=1
        else:
            dq_bridge.popleft()
            dq_bridge.append(0)
            dap +=1

print(dap)
