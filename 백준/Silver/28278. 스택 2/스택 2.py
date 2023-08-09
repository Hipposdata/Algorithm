import sys
def s(n):
    if n[0] ==1:
        stack.append(n[1])
    elif n[0]==2:
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack.pop())
    elif n[0] == 3:
        res.append(len(stack))
    elif n[0] == 4:
        if len(stack) == 0:
            res.append(1)
        else:
            res.append(0)
    elif n[0] == 5:
        if len(stack) ==0:

            res.append(-1)
        else:
            res.append(stack[-1])
stack = []
res = []
N = int(sys.stdin.readline())
for _ in range(N):
    n = list(map(int,sys.stdin.readline().split()))
    s(n)
for i in res:
    print(i)