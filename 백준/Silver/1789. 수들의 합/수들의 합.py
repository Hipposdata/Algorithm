import sys
n = int(sys.stdin.readline())  
hap = 0  # 합계
cnt = 0  # 자연수 개수

# 작은 수부터 차례대로 더하기
i = 1
while hap + i <= n:
    hap += i  # 현재 숫자 더하기
    cnt += 1  # 숫자 개수 증가
    i += 1    # 다음 숫자로 이동

print(cnt)  # 최대 개수 출력
# 어짜피 서로다른 수의 총 개수는 동일하므로 크거나 작은 최대값 개수만 알면됨