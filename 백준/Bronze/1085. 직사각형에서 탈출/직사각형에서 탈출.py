import sys

x, y , w, h = map(int,sys.stdin.readline().split())

a =[w-x,h-y,x,y]
print(min(a))