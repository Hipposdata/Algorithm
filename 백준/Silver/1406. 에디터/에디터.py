import sys
from collections import deque
N = str(sys.stdin.readline().rstrip()) # 개행문자 없이 입력받기 -> 있을경우 문자1개에서 B 입력시 개행문자가 지워지게됨
M = int(sys.stdin.readline()) # 반복 횟수

rgt = deque()
lft = deque(N)

for i in range(M):
    m = sys.stdin.readline().split()
    if m[0]== 'L':
        if len(lft) ==0:
            pass
        else:
            rgt.appendleft(lft[-1])
            lft.pop()
    elif m[0]== 'D':
        if len(rgt)==0:
            pass
        else:
            lft.append(rgt[0])
            rgt.popleft()
    elif m[0] == 'B':
        if len(lft) == 0:
            pass
        else:
            lft.pop()
    elif m[0] == 'P':
        lft.append(m[1])
hap= lft + rgt
dap = [e for e in hap if e != '\n']
print("".join(dap))