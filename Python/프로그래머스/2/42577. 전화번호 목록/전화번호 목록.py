def solution(phone_book):
    answer = True 
    phone_set = set(phone_book)
    
    # print(phone_set)
    
    for i in phone_book:
        stn = ""
        
        for num in i:
            stn += num
            
            if stn in phone_set and stn != i: # 자기자신은 포함 X 
                answer = False
    
    return answer