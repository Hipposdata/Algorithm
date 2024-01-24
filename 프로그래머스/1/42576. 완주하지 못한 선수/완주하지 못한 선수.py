def solution(participant, completion):
    answer = ''
    dic= {}    
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in completion:
        dic[j] -= 1
        
    for a,b in dic.items():
        if b != 0:
            answer =  a
    
        
    return answer