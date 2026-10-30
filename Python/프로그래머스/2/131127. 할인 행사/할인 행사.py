# for문 10일 롤링 윈도우 
# 해당 기간의 각 품목 개수, 넘버수 비교 -> 충족시 리솔트+=1

def solution(want, number, discount):
    answer = 0
    
    for i in range(0, len(discount)-10+1):
        for j in range(len(want)):
            flag = True
            if discount[i:i+10].count(want[j]) != number[j]:
                flag = False
                break
                
        if flag:
            answer += 1
        
    
    return answer