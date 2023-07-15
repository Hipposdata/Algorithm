import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

dap = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k :
                if lst[i] + lst[j]+lst[k] <= M:
                    dap.append(lst[i] + lst[j]+lst[k])

print(max(dap))