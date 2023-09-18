import sys

d, h, w = map(int,sys.stdin.readline().split())
tmp_d = ((h**2) + (w**2))**(1/2)

print(int((h*d)/tmp_d),int((w*d)/tmp_d))