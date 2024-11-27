import sys

n = int(sys.stdin.readline())

def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n-1)

print(int(fac(n) / (fac(5) * fac(n-5))))