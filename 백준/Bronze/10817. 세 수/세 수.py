import sys

a,b,c = map(int,sys.stdin.readline().split())

lst = [a,b,c]
print(sorted(lst)[1])
