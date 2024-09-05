
import sys
n = int(sys.stdin.readline())

start = 1 # 시작 인덱스 지우기
end = 1 # 끝 인덱스 지우기
sum = 1 # 시작과 끝 사이 총합
cont = 0 # 조건 만족시 카운트

while start <= n:
    # print(f"start: {start}")
    # print(f"end: {end}")
    # print(f"sum: {sum}")
    # print(f"cont: {cont}")
    # print("---------------")
    if sum == n:
        cont += 1
        sum -= start
        start += 1
    elif sum < n:
        end += 1
        sum += end
    else:  # sum > n
        sum -= start
        start += 1

print(cont)