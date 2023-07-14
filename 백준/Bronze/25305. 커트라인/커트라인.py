import sys
N, K = map(int, sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort(reverse=True)
lst = lst[K-1]

print(lst)

