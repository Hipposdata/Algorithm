# 유클리드 호제법
# 자릿수의 최대공약수를 구하고 그 자릿수만큼의 1로 이루어진 수를 출력하면 됩니다.
import sys

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

a, b = map(int, sys.stdin.readline().split())

print(gcd(a,b) *'1')
