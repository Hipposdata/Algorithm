import sys
from collections import deque
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

dq = deque( (i +1, lst[i] ) for i in range(len(lst)) ) # 풍선번호, 적힌숫자 순으로 저장

dap = [1]
num = dq[0][1]
dq.popleft()
while dq:
    if num >0:
        for _ in range(num):
            dq.append(dq[0])
            dq.popleft()
        num = dq[-1][1]

        dap.append(dq[-1][0])
        dq.pop()
    elif num < 0:
        for _ in range(-num):
            dq.appendleft(dq[-1])
            dq.pop()

        num = dq[0][1]
        dap.append(dq[0][0])
        dq.popleft()


for i in dap:
    print(i, end=' ')