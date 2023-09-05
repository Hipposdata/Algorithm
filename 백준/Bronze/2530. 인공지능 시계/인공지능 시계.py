import sys

a, b, c = map(int,sys.stdin.readline().split())
d = int(sys.stdin.readline())
sec = c + b *60 + a*60*60
d = sec+ d
s = d % 60
m = (d // 60) % 60
h = ((d // 60) // 60) % 24

print(h,m,s)