import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)
# 각 인덱스는의 값은 해당 숫자 연산의 최소 수

for i in range(2,n+1):

    # 1빼는 연산
    dp[i] = dp[i-1]+1
    # 2로 나눠지는 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] +1)
    # 3으로 나눠지는 연산
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])