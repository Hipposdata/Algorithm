def solution(n, times):
    answer = 0
    time = 0
    
    left = 1
    right =  min(times) * n
    
    while left<= right:
        time = (left + right) //2 
        
        cnt = 0
        for i in times:
            cnt += time // i
            
        if cnt < n:
            left = time +1
        else:
            right = time -1

    
    answer = left 
    
    return answer