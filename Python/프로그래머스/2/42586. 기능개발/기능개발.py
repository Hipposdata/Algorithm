def solution(progresses, speeds):
    answer = []
    num = []
    
    for p in range(len(progresses)):
        cnt = 0
        while True:
            if progresses[p] >=100:
                num.append(cnt)
                break
            progresses[p] += speeds[p]
            cnt +=1
            
    cnt2 = 1
    hap = num[0]
    
    for n in range(1, len(num)):
        if num[n] <=hap:
            cnt2+=1
        else:
            answer.append(cnt2)
            cnt2 = 1
            hap = num[n]
        
    answer.append(cnt2)
    return answer