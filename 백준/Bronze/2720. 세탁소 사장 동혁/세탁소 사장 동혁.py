import sys
N = int(sys.stdin.readline())
lst = []

for i in range(N):
    tmp = int(sys.stdin.readline())
    lst.append(tmp)
dap = []

for i in range(N):
    gap = lst[i]//25
    dap.append(gap)
    nam = lst[i]%25
    gap = nam//10
    nam = nam%10
    dap.append(gap)
    gap = nam//5
    nam = nam%5
    dap.append(gap)
    dap.append(nam)
    for j in range(4):
        print(dap[j], end=" ")
    print()
    dap = []