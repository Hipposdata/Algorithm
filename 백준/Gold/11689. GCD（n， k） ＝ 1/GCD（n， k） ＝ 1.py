
import sys
n = int(sys.stdin.readline())
sosu_cont = n

# 입력값의 소수개수만 알면 되므로 각각 계산해줌
for j in range(2, int(n**0.5)+1):
    if n % j ==0: # 소인수 확인
        sosu_cont = sosu_cont - int(sosu_cont/j)
        while n % j == 0: # 다음 소인수 n 찾기
            n = n // j

# 루트까지 확인하고 남은 소인수1개 n 확인(루트까지 반복해도 없다면
# 최초입력받은 n자체가 소인수임
if n >1:
    sosu_cont = sosu_cont - int(sosu_cont / n)
print(sosu_cont)