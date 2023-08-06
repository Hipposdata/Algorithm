import sys

def gcd(a,b):
    if b == 0:
        return a
    r = a%b
    if r !=0:
        a,b = b, r
        return gcd(a,b)
    else:
        return b

T = int(sys.stdin.readline())

for i in range(T):
    a , b = map(int,sys.stdin.readline().split())
    print(int((a*b)/gcd(a,b)))