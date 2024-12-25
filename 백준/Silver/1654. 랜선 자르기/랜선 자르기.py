# 이진탐색 이용
import sys

k, n = map(int,sys.stdin.readline().split())

lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline().strip()))

l, h = 1, max(lst)
rst = 0
while l <= h:
    mid = (l + h) // 2
    hap = sum([i // mid for i in lst]) # 랜선개수 총합

    if hap >= n:
        rst = mid
        l= mid +1
    else:
        h = mid -1

print(rst)