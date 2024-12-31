# import sys
# sys.setrecursionlimit(10**6)
# n = int(sys.stdin.readline())
#
# # 모든 수를 반복하면서 조건에 부합하면 카운트하기
# # 재귀식으로 이진수 만들기
#
# lst = []
# num = '1'
# length = 0
# def bi(num, n):
#     if len(num) == n: # 자리수 만족시 추가
#         lst.append(num)
#     else:
#         bi(num+'1',n)
#         bi(num+'0',n)
#
# bi(num,n)
# cnt = 0
# for i in lst:
#     if '11'  not in i:
#        cnt+=1
# print(cnt)
# ######### 메모리 초과
# dp 이용
import sys
# 2차원 배열 dp -> 1로 끝, 0으로 끝
# 0은 2개 가능 / 1은 앞자리 0인 한개만 가능
n = int(sys.stdin.readline())

dp = [[0,0] for col in range(n+1)]

dp[1][0] = 0
dp[1][1] = 1
# dp[행][열]
# 0은 이전값 둘다 가능 / 1은 이전값 0만 가능
for i in range(2,n+1):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]

print(dp[n][0]+dp[n][1])


