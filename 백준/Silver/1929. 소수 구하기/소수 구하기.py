# 정수론 소수구하기
import sys
m, n = map(int,sys.stdin.readline().split())



lst = [0] *2 + [1] * (n-1)

for j in range(2, int(n**(1/2))+1 ):
    for k in range(j*j,n+1,j):
        lst[k] = 0

for l in range(2, n+1):
    if l >= m and lst[l] == 1:
        print(l)