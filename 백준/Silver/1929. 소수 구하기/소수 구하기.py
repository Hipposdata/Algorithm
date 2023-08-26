import sys

#  약수가 존재하면 소수가 아님을 이용
m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i %j ==0:
            break
    else:
        print(i)
