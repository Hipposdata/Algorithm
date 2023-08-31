import sys

sum, dif = map(int,sys.stdin.readline().split())

a = (sum+dif)//2
b = (sum-dif)//2

if sum < dif :
    print(-1)
else:
    if (a + b) == sum and a - b == dif: # 조건 맞는지 확인 
        print(a, b)
    else:
        print(-1)