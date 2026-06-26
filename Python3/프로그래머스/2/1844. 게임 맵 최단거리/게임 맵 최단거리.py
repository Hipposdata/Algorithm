from collections import deque

def solution(maps):
    answer = 0
    row_len = len(maps)
    col_len = len(maps[0])
    
    # 방향정의 하좌상우
    dr = [1,0,-1,0]
    dc = [0, -1,0,1]
    
    # 최단거리 -> bfs
    q = deque()
    q.append((0,0,1))

    # 방문기록 
    vst = [ [False] * col_len for _ in range(row_len)]
    vst[0][0] = True
    
    # 큐에 좌표, 거리 넣음
    while q:
        cur_r, cur_c, dist = q.popleft()
        
        if cur_r == row_len-1 and cur_c == col_len -1:
            break
        
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            # 범위 내
            if 0<=nr <=row_len-1 and 0<=nc<=col_len-1:
                
                # 장애물X, 방문X 
                if vst[nr][nc] ==False and maps[nr][nc] ==1:
                    vst[nr][nc] = True
                    q.append((nr, nc, dist +1))            
                    
    if vst[-1][-1] == False:
        answer = -1
    else:
        answer = dist
    return answer