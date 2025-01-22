import sys

x,y,w,s = map(int,sys.stdin.readline().split())

# 3 케이스 중 최소값 출력
# 1. 가로세로로만 이동
a = (x+y)*w
# 2. 대각선으로만 이동 - 합이 짝수여야함

if (x+y) %2 == 0: # 짝수인경우
    b =  max(x,y) * s
else: # 홀수인경우 최대한 대각선이동 + 한칸은 가로세로
    b = (max(x,y) -1) * s + w
# 3. 대각선 + 가로세로 이동

c = min(x,y) * s + abs(x -y) * w

print(min(a,b,c))