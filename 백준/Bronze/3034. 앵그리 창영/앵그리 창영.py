import sys

n,w,h = map(int, sys.stdin.readline().split())

for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num <= (w**2 + h**2)**(1/2):
        print('DA')
    else:
        print('NE')