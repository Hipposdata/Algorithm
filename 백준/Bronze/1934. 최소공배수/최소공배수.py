# 유클리드 호제법
import sys
t = int(sys.stdin.readline())

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(int(a*b / gcd(a,b)))