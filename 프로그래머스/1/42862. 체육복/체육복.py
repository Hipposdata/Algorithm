def solution(n, lost, reserve):
    num = [1] * (n+2)
    for i in lost:
        num[i] -= 1
    for i in reserve:
        num[i] += 1
    print(num)
    for i in range(1, n+1):
        if num[i-1] ==0 and num[i] == 2:
            num[i-1], num[i] = 1, 1
        elif num[i] == 2 and num[i+1] == 0:
            num[i], num[i+1] = 1,1
    answer = 0
    for i in num[1:-1]:
        if i == 1 or i == 2:
            answer +=1
    
    return answer