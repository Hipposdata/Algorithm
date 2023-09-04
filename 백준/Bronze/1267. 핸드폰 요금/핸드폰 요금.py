import sys

n = int(sys.stdin.readline())
t = list(map(int,sys.stdin.readline().split()))

y = 0
m = 0
for i in t:
    y += ((i//30) +1) * 10
    m += ((i//60) +1) * 15

if y > m :
    print('M', m)
elif y < m :
    print('Y', y)
else:
    print('Y','M',y)