import sys

# n행 m열 입력 받기
n, m = map(int, sys.stdin.readline().split())
chess = []

# 체스판 입력 받기
for _ in range(n):
    chess.append(sys.stdin.readline().strip())

# 최소 칠해야 하는 횟수를 구할 리스트
lst = []

# 8x8 부분을 찾아서 w와 b 칠하는 횟수 계산
for row in range(n - 8+1):
    for col in range(m - 8+1):
        w_cnt = 0  # 'W'가 첫 번째로 나오는 경우
        b_cnt = 0  # 'B'가 첫 번째로 나오는 경우

        # 8x8 크기의 체스판 구간을 확인
        for i in range(8):
            for j in range(8):
                # (i + j) % 2 == 0이면 첫 번째 색상, 나머지 색상은 다른 색상
                # 아니면 이중 조건문으로 표현 가능 4 case
                if (i + j) % 2 == 0:
                    if chess[row + i][col + j] != 'W':
                        w_cnt += 1
                    if chess[row + i][col + j] != 'B':
                        b_cnt += 1
                else:
                    if chess[row + i][col + j] != 'B':
                        w_cnt += 1
                    if chess[row + i][col + j] != 'W':
                        b_cnt += 1

        # 두 경우 중 더 적은 횟수를 선택
        lst.append(min(w_cnt, b_cnt))

# 결과 출력
print(min(lst))
