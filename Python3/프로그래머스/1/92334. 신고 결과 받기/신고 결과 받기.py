def solution(id_list, report, k):
    answer = []
    dic = {}
    dic_mail = {}
    report = set(report)
    
    for i in id_list:
        dic[i] = 0     
        dic_mail[i] = 0
    
    # 신고당한 횟수
    for r in report:
        a,b = r.split()
        dic[b] +=1
        
        
    for r in report:
        a,b = r.split()            
        if dic[b] >=k:
            dic_mail[a] +=1
    
    for j in id_list:
        answer.append(dic_mail[j])
        
    return answer