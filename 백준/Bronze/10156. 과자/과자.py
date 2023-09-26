import sys

k, n ,m = map(int,sys.stdin.readline().split())

if k*n-m <=0:
    print(0)
else:
    print(k*n-m)
