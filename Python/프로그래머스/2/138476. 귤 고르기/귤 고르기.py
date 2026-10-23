def solution(k, tangerine):
    answer = 0
    # 서로 다른 귤 종류 많은 순서대로 정렬 
    # 하나씩 차감해가면서 k선택할 시, 서로다른거 개수세기
    
    dic = {}
    for i in tangerine:
        dic[i] = 0
    for j in tangerine:
        dic[j] += 1
    
    
    dic = sorted(dic.items(), key = lambda x: x[1], reverse =True)
    
    cnt = 0
    hap = 0
    for a,b in dic:
        if hap < k:
            cnt+=1
            hap+=b
    answer = cnt
    return answer