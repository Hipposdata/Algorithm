import sys

n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
mlist = list(map(int,sys.stdin.readline().split()))

ndic= {}

dap = []
for i in nlist:
    if i in ndic:
        ndic[i] += 1
    else:
        ndic[i] = 1
for i in mlist:
    if i in ndic:
        dap.append(ndic[i])
    else:
        dap.append(0)
for i in dap:
    print(i, end=" ")