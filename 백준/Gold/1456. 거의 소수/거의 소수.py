# 정수론 소수구하기
import sys
a,b = map(int,sys.stdin.readline().split())

n = int(b**(1/2)) +1

lst = [0] *2 + [1] * (n-1)

for j in range(2, int(n**(1/2))+1 ):
    for k in range(j*j,n+1,j):
        lst[k] = 0

cont = 0
for l in range(2, n+1):
    if lst[l] == 1:
        x = 2
        while l**x <= b:
            if l**x >=a :
                cont += 1
            x+=1

print(cont)