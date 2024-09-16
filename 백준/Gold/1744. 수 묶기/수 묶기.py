#음수, 0 양수 따로 저장
# 음수끼리 작은 두수끼리 묶음 / 양수끼리 큰 두수끼리 묶음
# 0은 음수 1개 남을 시 묶음
import sys
import heapq

n = int(sys.stdin.readline())

lst_neg = []
lst_pos = []
lst_zero = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num < 0:
        heapq.heappush(lst_neg, num)
    elif num >0: # 양수는 음수로 변환해서적재 -> 작은수부터빠지므로
        heapq.heappush(lst_pos, -num)
    else: # ==0
        heapq.heappush(lst_zero, num)

# 두수 중 하나이상 1일경우 더하는게 더 큼 곱하는것보다
sum_pos = 0
while len(lst_pos) >1:
    tmp1 = -heapq.heappop(lst_pos)
    tmp2 = -heapq.heappop(lst_pos)
    if tmp1 == 1 or tmp2 == 1:
        sum_pos += (tmp1 + tmp2)
    else:
        sum_pos += (tmp1 * tmp2)

if lst_pos:
    sum_pos += -heapq.heappop(lst_pos)

sum_neg = 0
while len(lst_neg) >1:
    tmp1 = heapq.heappop(lst_neg)
    tmp2 = heapq.heappop(lst_neg)
    sum_neg += (tmp1 * tmp2)

if len(lst_zero) == 0 and len(lst_neg) > 0 :
    sum_neg += heapq.heappop(lst_neg)

print(sum_pos + sum_neg)