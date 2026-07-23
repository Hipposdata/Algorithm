def solution(numbers, target):
    answer = 0
    
    sm = [0]
    
    for i in numbers:
        
        nxt_sm = []
        
        for j in sm:
            nxt_sm.append(j + i)    
            nxt_sm.append(j - i)
            
        sm = nxt_sm

    
    return sm.count(target)