def solution(citations):
    answer = 0
    h_up = 0

    
    for i in range(len(citations), -1, -1):
        flag = True
        cnt_a = 0
        cnt_b = 0
        for j in citations:
            if j >=i :
                cnt_a += 1
            else:
                cnt_b +=1
                
        if cnt_a >= i and cnt_b <=i:
            answer = i
            break
    
    return answer