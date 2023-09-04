import sys

m = int(sys.stdin.readline())

cup = [0,1,0,0]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    cup[x], cup[y] = cup[y], cup[x]

print(cup.index(1))