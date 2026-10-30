# dic 형식 신고당한자:신고한자


def solution(id_list, report, k):
    answer = []
    # 딕셔너리 생성 
    dic = {}
    tmp = {}
    for j in id_list:
        dic[j] =[]
        tmp[j] = 0
        
    # print(dic)

    
    for i in report:
        a,b = i.split()[0], i.split()[1]
        
        dic[b].append(a)
    
    # print(dic)
    

    # 개수 세기 
    for ky,v in dic.items():
        if len(set(dic[ky])) >= k:
            for t in set(v):
                tmp[t] +=1
                
    for q,w in tmp.items():
        answer.append(w)

        
    return answer