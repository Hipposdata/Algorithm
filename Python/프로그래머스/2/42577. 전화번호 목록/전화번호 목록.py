def solution(phone_book):
    answer = True
    dic = {}

    # 딕셔너리구조
    for i in phone_book:
        dic[i] = 0
    # print(dic)
    
    for j in phone_book:
        tmp = ''
        for stn in j:
            tmp += stn
            if tmp in dic and tmp != j:
                answer = False
        

    
    return answer