# 36진법 -> 10진법변환
# zzz 36
# 35*36**2 + 35*36**1 + 35*36**0 -> 앞에서부터 승수작아지므로 뒤집기
import sys
N, B = sys.stdin.readline().split()
N = str(N)
B = int(B)

N = N[::-1]
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dap = 0
for i in range(len(N)):
    for j in range(36):
        if num[j] == N[i]:
            dap += (B**i)*j
print(dap)