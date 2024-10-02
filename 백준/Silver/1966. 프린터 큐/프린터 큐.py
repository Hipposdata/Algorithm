import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int,sys.stdin.readline().strip().split())
    lst = list(map(int, sys.stdin.readline().strip().split()))
    deq = deque(lst)
    idx = m # 찾을 문서 위치 -> 계속변함
    dap = 1 # 문서 인쇄 횟수
    while True:
        if idx == 0 and max(deq) == deq[idx]:
            break
        if deq[0] == max(deq):
            deq.popleft()
            dap +=1
            if idx ==0:
                idx =len(deq) -1
            else:
                idx -=1
        elif deq[0] != max(deq):
            deq.append(deq[0])
            deq.popleft()
            if idx ==0:
                idx =len(deq) -1
            else:
                idx -=1
    print(dap)