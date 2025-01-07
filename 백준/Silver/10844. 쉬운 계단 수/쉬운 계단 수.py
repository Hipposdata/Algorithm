import sys

n = int(sys.stdin.readline())

dp = [[0 for i in range(11)] for j in range(n+1)]
# dp[n][끝나는 수 0~ 9]
for i in range(1,9+1): # dp[1] n=1인 경우는 1~9  1
    dp[1][i] = 1


for j in range(2, n+1):
    dp[j][0] = dp[j-1][1] # 0으로 끝나면 전 값 1에서 0으로 가는 경우
    dp[j][9] = dp[j-1][8] # 9로 끝나면 전 값 8에서 9로 가는 경우
    for k in range(1,8+1):
        dp[j][k] = dp[j-1][k-1] + dp[j-1][k+1] # 1~8은 +=1 두케이스

hap = 0
for q in range(0,9+1):
    hap += dp[n][q]
print(hap % 1000000000)