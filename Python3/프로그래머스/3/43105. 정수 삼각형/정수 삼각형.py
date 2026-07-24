def solution(triangle):
    # 원본을 보존하기 위해 복사
    # print(row)
    dp = [row[:] for row in triangle]

    for r in range(1, len(dp)):
        for c in range(r + 1):

            # 가장 왼쪽: 오른쪽 위에서만 내려올 수 있음
            if c == 0:
                dp[r][c] += dp[r - 1][c]

            # 가장 오른쪽: 왼쪽 위에서만 내려올 수 있음
            elif c == r:
                dp[r][c] += dp[r - 1][c - 1]

            # 가운데: 위쪽 두 경로 중 큰 값 선택
            else:
                dp[r][c] += max(
                    dp[r - 1][c - 1],
                    dp[r - 1][c]
                )

    return max(dp[-1])