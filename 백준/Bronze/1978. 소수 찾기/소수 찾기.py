import sys
N = int(sys.stdin.readline())
sosu = list(map(int,sys.stdin.readline().split()))

# 소수확인 함수 
def find_sosu(n):     
    hap = []
    for i in range(1,n+1):
        if n % i == 0:
            hap.append(i)
    if len(hap) ==2:
        return n

count = 0   # 반복문으로 소수확인, 카운트 
for i in range(len(sosu)):   
    if find_sosu(sosu[i]) != None:
        count +=1

print(count)

