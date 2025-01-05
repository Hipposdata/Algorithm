import sys
# 1 1 / 2 2 / 3 3 / 4 5 /
# 전의 두항 더하면 현재 항 구할 수 있음
n = int(sys.stdin.readline())

dp = [0] *(n+2) # n+1 까지 만들경우 n ==1일때 인덱스에러 발생
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])