# 큰숫자 우선순위 높음 

from collections import deque

def solution(priorities, location):
    
    q = deque([(i,v) for i, v in enumerate(priorities)])    
    
    cnt = 0
    while True:
        cur = q.popleft()

        if len(q) >0:
            
            if cur[1] < max(q, key =  lambda x: x[1])[1]:
                q.append(cur)
            else: # 우선순위 큰값인 경우 빼기 
                cnt+=1

                if cur[0] == location :
                    break
        else:
            cnt +=1
            break            
                    
    return cnt