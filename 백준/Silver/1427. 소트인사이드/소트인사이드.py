#선택정렬
import sys

n = list(map(int,sys.stdin.readline().strip()))

for idx in range(len(n)):
    mx_idx = n[idx:].index(max(n[idx:])) + idx
    if n[mx_idx] > n[idx]:
        n[mx_idx], n[idx] = n[idx], n[mx_idx]

print(''.join(map(str,n)))