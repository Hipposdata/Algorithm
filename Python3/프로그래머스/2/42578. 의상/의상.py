
def solution(clothes):
    answer = 0
    dic = {}
    
    for cat, kind in clothes:
        dic[kind] = dic.get(kind, 0) + 1
        
    answer = 1
    
    for cnt in dic.values():
        answer *= (cnt+1)
    
    
    return answer -1