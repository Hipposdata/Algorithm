import sys
def gcd(a,b):  # 유클리드 호제법 -> 최대공약수
    if b == 0:
        return a
    r = a%b
    if r !=0:
        a,b = b, r
        return gcd(a,b)
    else:
        return b

a , b = map(int,sys.stdin.readline().split())
print(int((a*b)/gcd(a,b)))  # 최소공배수 = a*b/최대공약수
