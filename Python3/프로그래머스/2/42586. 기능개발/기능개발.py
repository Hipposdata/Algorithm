from collections import deque

def solution(progresses, speeds):   
    day = 0
    lst = []
    
    
    
    
    for i in range(len(progresses)):
        
        if progresses[i] + day * speeds[i] >=100 :
            lst[-1] +=1
        
        else:
        
            while progresses[i] + (day * speeds[i]) < 100:
                day+=1
            lst.append(1)

    
    return lst