import sys
# 제일 큰 c가 나머지 a,b의 합보다 작아야함
n = int(sys.stdin.readline())
cnt = 0

for a in range(1,n-1):
    for b in range(a,n-a):
        c = n-(a+b)
        if b > c:
            break
        if a+b >c and a <=c and b<=c:
            cnt +=1
# 정렬 후 중복값 제거
print(cnt)

