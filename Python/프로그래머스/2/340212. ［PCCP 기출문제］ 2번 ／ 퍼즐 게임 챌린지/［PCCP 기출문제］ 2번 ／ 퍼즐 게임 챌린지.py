def solution(diffs, times, limit):
    
    left = 1
    right = max(diffs)
    
    while left <= right:
        i = (left + right) //2

        time = diffs[0] * times[0]
        
        for idx in range(1,len(diffs)):
            # 레벨보다 큰 경우 
            if i >= diffs[idx]:
                time += times[idx] 
            # 레벨보다 작은경우
            
            else:
                time += (diffs[idx] - i) * (times[idx-1] + times[idx]) + times[idx]
        
            if time > limit:
                break 
        if time <= limit:
            right = i -1
            
        else:
            left = i +1
            
    return left