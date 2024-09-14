# greedy
import sys
n, k = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

cont = 0
for i in reversed(lst):
    if k // i >0:
        cont += k // i
        k %= i
    if k ==0:
        break
print(cont)