def solution(n, computers):
    
    vst = [False] * n
    answer = 0
    
    # 컴퓨터 하나씩 방문
    for i in range(n):
        
        # 방문X -> +1
        if vst[i] == False:
            answer +=1
        elif vst[i] == True:
            continue
        
        stck = [i]
        vst[i] = True
        
        # 전체 탐색
        while stck:
            cur = stck.pop()
            
            # 노드 순회 
            for nxt in range(n):
                # 노드 연결된 경우 
                if computers[cur][nxt] ==1:
                    # 연결됐는데 방문기록 없으면 -> 방문처리 
                    if vst[nxt] == False:
                        vst[nxt] = True
                        stck.append(nxt)
    

    return answer