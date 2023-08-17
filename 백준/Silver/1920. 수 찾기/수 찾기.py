import sys

n = int(sys.stdin.readline())
n2 = set(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m2 = list(map(int,sys.stdin.readline().split()))

for i in m2:
    if i in n2:
        print(1)
    else:
        print(0)