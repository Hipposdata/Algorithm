import sys
n,m = map(int,sys.stdin.readline().split())

limit = []
real = []
s = 0
for _ in range(n):
    s1, s2 = map(int, sys.stdin.readline().split())
    s +=s1
    limit.append((s,s2))
s = 0
for _ in range(m):
    s1, s2 = map(int, sys.stdin.readline().split())
    s +=s1
    real.append((s,s2))

dap = []
idx_r = 0
idx_l = 0
n = 0
while True:
    n += 1
    dap.append(real[idx_r][1] - limit[idx_l][1])
    if n == real[idx_r][0]:
        idx_r+=1
    if n == limit[idx_l][0]:
        idx_l+=1
    if n == 100:
        break
if max(dap) <= 0:
    print(0)
else:
    print(max(dap))

# 일일히 하나씩 더해주면서 계산해주기
# 2 2
# 1 10
# 99 20
# 1 100
# 99 30