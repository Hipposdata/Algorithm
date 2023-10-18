import sys

a,b = map(int,sys.stdin.readline().split())
if a %4 ==0:
    print(abs(b % 4 - 4) + abs(b // 4 - ((a // 4)-1)))
elif b % 4 ==0:
    print(abs(4 - a % 4) + abs(((b // 4)-1) - a // 4))
else:
    print(abs(b % 4 - a % 4) + abs(b // 4 - a // 4))