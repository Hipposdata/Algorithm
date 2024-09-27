import sys
n = int(sys.stdin.readline())


a = 0
b = 0
c = 0


if n >= 300:
    a = n // 300
    n = n % (300*a)
if n >= 60:
    b = n // 60
    n = n% (60*b)
if n < 60:
    c = n // 10
    # n = n % (10*c)

if n % 10 !=0:
    print(-1)
else:
    print(a, b, c)

