# 빠르게 도달 -> BFS

from collections import deque 

def solution(maps):
    answer = 0
    
    col = len(maps[0])
    row = len(maps)
    
    # 방문기록 
    vst = [[False] * col for _ in range(row)]
    vst[0][0] = True
    
    # 방향지정 하좌상우
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    
    # 위치 이동수  / 첫칸은 1 
    step = [[1] * col for _ in range(row)]
    
    q = deque()
    q.append((0,0))
    
    while q:
        cur_r, cur_c = q.popleft()
        
        # 마지막 도착지 방문 -> 멈춤
        if vst[row-1][col-1] == True:
            break
        
        # 다음 이동위치 선정 
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            
            # 범위내
            if 0<=nr<= row-1 and 0<= nc <=col-1:
                # 방문X
                if vst[nr][nc] == False:
                    # 벽 없음
                    if maps[nr][nc] == 1:
                        step[nr][nc] = step[cur_r][cur_c] +1
                        vst[nr][nc] = True
                        q.append((nr, nc))
        if vst[row-1][col-1] == False:
            answer = -1
        else:
            answer = step[row-1][col-1]
    
    
    return answer