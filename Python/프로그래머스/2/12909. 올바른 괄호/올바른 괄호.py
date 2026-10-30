

def solution(s):
    answer = True
    stck = []
    
    for i in s:
        if i == '(':
            stck.append(s)
        else:
            if len(stck) == 0:
                answer = False
                break
            stck.pop()
            
    if len(stck) >0:
        answer = False
    
    return answer