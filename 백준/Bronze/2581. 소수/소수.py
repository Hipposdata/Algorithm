import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

# 소수확인 함수
def find_sosu(n):
    hap = []
    for i in range(1,n+1):
        if n % i == 0:
            hap.append(i)
    if len(hap) ==2:
        return n

sosu_lst = []     # 소수인것들 리스트에 담기
for i in range(M, N+1):
    if find_sosu(i) != None:
        sosu_lst.append(i)

if len(sosu_lst) ==0:  
    print(-1)
else:
    print(sum(sosu_lst))
    print(min(sosu_lst))