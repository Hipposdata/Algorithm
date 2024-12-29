import sys
import heapq
n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(lst,x)
    elif x == 0:
        if len(lst) !=0:
            print(heapq.heappop(lst))
        else:
            print(0)



