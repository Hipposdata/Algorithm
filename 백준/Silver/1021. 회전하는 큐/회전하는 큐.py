import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

deque = deque(i for i in range(1,n+1) )

dap = 0
for i in lst:
    if i == deque[0]:
        deque.popleft()
    else:
        if deque.index(i) < len(deque) - deque.index(i): # 2번작업수행
            while i != deque[0]:
                deque.append(deque[0])
                deque.popleft()
                dap +=1
            deque.popleft() # i == deque[0]
        else: # 3번작업 수행
            while i != deque[0]:
                deque.appendleft(deque[-1])
                deque.pop()
                dap +=1
            deque.popleft() # i == deque[0]

print(dap)