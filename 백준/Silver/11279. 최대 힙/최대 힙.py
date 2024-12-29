import sys
import heapq
n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(lst,-x) # 음수로 바꿔서 출력
    elif x == 0:
        if len(lst) !=0:
            print(-heapq.heappop(lst)) # 작은값부터 출력되므로 큰순서대로 출력됨(-로 원본으로 바꿔출력)
        else:
            print(0)


