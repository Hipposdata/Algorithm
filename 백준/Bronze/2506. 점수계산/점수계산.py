import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

hap = 0
dap = 0
for i in range(n):
    if lst[i] == 1:
        hap +=1
        dap += hap
    if lst[i] ==0:
        hap = 0
print(dap)