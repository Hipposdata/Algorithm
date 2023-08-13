import sys
def fac(a):
    for i in range(1,a):
        a *= i
    return a

n , m = map(int,sys.stdin.readline().split())

if m == 0 :
    print(1)
elif m == n:
    print(1)
else:
    print((fac(n)//(fac(n-m)*fac(m)))%10007)