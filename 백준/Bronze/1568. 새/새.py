N = int(input())
i =1
sm = 0 # 하나씩 세줌
tf = True
while tf :
    if N < i: # 남은 새의 수보다 빼야될 새의 수가 큰경우 다시 1로 초기화
        i=1
    N-=i # 새를 오름차순으로 빼줌
    i+=1
    sm +=1 # 카운트
    if N<=0: # 종료
        tf = False
print(sm)