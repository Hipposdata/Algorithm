import sys

n = int(sys.stdin.readline())
lst =[0]
for _ in range(n):
    t,p = map(int,sys.stdin.readline().split())
    lst.append((t,p))

dp = [0]*(n+2) # 퇴사일은 하루다음이므로 +1/i번째일 부터 퇴사까지 얻을 수 있는 최대수익 -> 앞으로 갈수록 누적됨

dp[1] = 0

for i in range(n,0,-1):
    if lst[i][0] + i >n+1: # 상담일이 퇴사일 초과한 경우
        dp[i] = dp[i+1]
    else: # 상담일이 퇴사일 이내 이뤄짐
        dp[i] = max(dp[i+1],dp[i+lst[i][0]]+lst[i][1])

print(dp[1])


