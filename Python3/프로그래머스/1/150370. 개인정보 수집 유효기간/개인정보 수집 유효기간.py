def solution(today, terms, privacies):
    answer = []
    
    # 1. 수식 전체를 괄호로 묶어 줄바꿈 에러 해결
    td = ( (int(today[0:4])) * 336 
         + (int(today[5:7])-1) * 28  
         + (int(today[8:10])) )
    
    for p_idx, j in enumerate(privacies):
        for i in terms:
            if i[0] == j[-1]:

                pd = (int(j[0:4])) * 336 + (int(j[5:7])-1) * 28 + (int(j[8:10])) + int(i[2:]) * 28 
    
                if td >= pd:

                    answer.append(p_idx + 1)
                    
    return answer