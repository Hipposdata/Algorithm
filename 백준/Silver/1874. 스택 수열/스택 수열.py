import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

stack = []
dap = []
num = 1

for j in lst:
    while num <= j:
        stack.append(num)
        dap.append('+')
        num += 1
    if stack[-1] == j:
        stack.pop()
        dap.append('-')
    elif stack[-1] != j:   # if stack[-1] != j -> 이러면 에러발생
        dap = ['NO']
        break

for k in dap:
    print(k)