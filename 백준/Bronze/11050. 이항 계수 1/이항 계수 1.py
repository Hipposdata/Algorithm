import sys
n, r = map(int,sys.stdin.readline().split())
def fac(num):
    if num <=0:
        return 1
    return num * fac(num-1)
print(int(fac(n)/ (fac(n-r) * fac(r))))