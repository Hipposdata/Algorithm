import sys
n , m = map(int,sys.stdin.readline().split())
a = n-m
for i in range(1,n):
    n *=i
for i in range(1,m):
    m*=i
for i in range(1, a):
    a *=i

print(n//(a*m))