import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

dap = 0
for idx in range(len(lst)):
   dap += lst[idx] *(len(lst) - idx)

print(dap)