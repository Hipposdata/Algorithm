def solution(progresses, speeds):
    answer = []
    
    idx = 0
    while True:
        if all(list(map(lambda x: x>=100 , progresses))):
            break
        print(progresses)
        
        for j in range(len(speeds)):
            progresses[j] += speeds[j]
        
        cnt = 0
        # 인덱스 0부터 차례대로 확인 -> 100넘는경우 다음 인덱스 통과 
        
        # idx 기준부터 확인하기
        for i in range(idx, len(progresses)):
            if progresses[i] >=100:
                idx +=1
                cnt+=1
            else:
                break

        if cnt> 0:
            answer.append(cnt)
        print(answer)

                
    return answer