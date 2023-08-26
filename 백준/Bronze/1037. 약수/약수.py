import sys

n = int(sys.stdin.readline())
yaklst = list(map(int,sys.stdin.readline().split()))
print(max(yaklst)* min(yaklst))