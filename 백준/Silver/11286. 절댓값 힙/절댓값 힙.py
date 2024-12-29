import sys
import heapq
n = int(sys.stdin.readline())
# 힙구조 정렬 사전식순서 -> 튜플 요소 앞순서부터 정렬됨
lst = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(lst,(abs(x),x)) # 튜플형식으로 삽입
    elif x == 0:
        if len(lst) !=0:
            print(heapq.heappop(lst)[1]) # 두번째 요소인 원본 출력
        else:
            print(0)


