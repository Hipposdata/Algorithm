def solution(today, terms, privacies):
    answer = []
    # 딕셔너리화
    dic = {}
    for j in terms:
        a,b = j.split()
        dic[a] = b
    print(dic)
    
    to_lst = list(map(int, today.split('.')))
    cnt_to = to_lst[0]*28*12 + to_lst[1] *28 + to_lst[2]

    
    for i in range(len(privacies)):
        a, b = privacies[i].split()
        lst = list(map(int, a.split('.')))
        cnt = lst[0] * 28*12 + lst[1] * 28 + lst[2]
        print(cnt_to)
        print(cnt + int(dic[b]))
        
        if cnt_to >= cnt + (int(dic[b])*28):
            answer.append(i+1)
    
    
    return answer