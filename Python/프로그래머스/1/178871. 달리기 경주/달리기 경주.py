def solution(players, callings):
    answer = []
    
    dic = {}
    
    cnt = 0
    for a in players:
        dic[a] = cnt
        cnt+=1        
    num = 0
    for i in callings:
            # 바로 앞 순위인 경우
        dic[players[dic[i] - 1]] +=1
        
        players[dic[i] - 1], players[dic[i]] = players[dic[i]], players[dic[i] - 1]

        dic[i] -=1
        
    answer = list(dict(sorted(dic.items(), key = lambda x : x[1])).keys())

    
    
    return answer