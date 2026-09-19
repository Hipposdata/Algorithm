# 방문 X -> 네트워크 +1 -> 탐색후 주변연결된 컴퓨터 방문처리 
def solution(n, computers):
    answer = 0
    
    vst = [False] * n
    
    for i in range(n):
        if vst[i] == False:
            answer += 1
            vst[i] = True
            
            stck = []
            stck.append(i)
            
            while stck:
                cur = stck.pop()
                
                for nxt in range(n):
                    if computers[cur][nxt] ==1 and vst[nxt] == False:
                        vst[nxt] = True
                        stck.append(nxt)
                        

        
    return answer