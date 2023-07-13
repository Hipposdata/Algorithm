import sys
N = int(sys.stdin.readline())
dap = []
for i in range(N):
    hap = sum(map(int,str(i)))
    if i + hap == N:
        dap.append(i)
        break
    if i + hap != N:
        dap.append(0)

if dap[-1] != 0:
    print(dap[-1])
else:
    print(0)