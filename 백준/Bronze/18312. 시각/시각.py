
n, k = map(int,input().split())

cnt = 0 # 개수 셀 변수 생성
for hour in range(0,n+1):
    if hour <= 9:
        hour = '0' + str(hour)
    for minute in range(0,60):
        if minute <= 9:
            minute ='0'+ str(minute)
        for second in range(0,60):
            if second <= 9:
                second = '0' + str(second)
            if str(k) in str(hour) + str(minute) + str(second):
                cnt +=1
print(cnt)