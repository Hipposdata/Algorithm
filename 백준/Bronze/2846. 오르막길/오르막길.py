import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
temp = []

for i in range(n):
    temp.append(0)

for i in range(0,n-1):
    if lst[i] < lst[i+1]:
        temp[i+1] = lst[i+1] - lst[i]

dap = []
for i in temp:
    if i == 0:
        dap.append(0)
    elif i >0:
        dap[-1] += i

print(max(dap))