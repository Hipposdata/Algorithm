import sys
input = sys.stdin.readline

n , m = map(int, input().split())
lst = list(map(int, input().split()))

# 누적합 배열 만들고
lst_hap = []
tmp = 0
for k in lst:
    tmp += k
    lst_hap.append(tmp)

# SUM 함수 사용시 시간초과
# for _ in range(m):
#     i, j = map(int, input().split())
#     print(sum(lst[i-1:j]))

# 합 배열에서 구간합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(lst_hap[j-1])
    else:
        print(lst_hap[j-1] - lst_hap[i-2])