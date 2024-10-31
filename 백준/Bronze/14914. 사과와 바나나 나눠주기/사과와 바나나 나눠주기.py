import sys

a,b = map(int, sys.stdin.readline().split())

if a > b:
    n = a
else:
    n = b

for i in range(1,n+1):
    if a%i== 0 and b %i == 0:
        print(i, a//i, b//i)