import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

lst.sort()

hap = []
for i in range(n):
    hap.append(lst[i] + lst[2*n-i-1])

print(min(hap))