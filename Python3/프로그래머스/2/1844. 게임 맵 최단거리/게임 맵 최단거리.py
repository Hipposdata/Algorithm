# 최솟값 -> bfs 

from collections import deque

def solution(maps):
    answer = 0
    # 방향 하좌상우
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    
    q = deque()
    q.append((0,0))
    
    # 행, 열 길이
    n = len(maps)
    m = len(maps[0])
    
    # 방문기록
    vst = [[False] * m for _ in range(n)]
    vst[0][0] = True
    
    # 해당위치 이동 수
    step = [[1] * m for _ in range(n)]
    
    # 행, 열 길이
    n = len(maps)
    m = len(maps[0])
    
    while q:
        cur_r, cur_c = q.popleft()
        
        if vst[n-1][m-1] == True:
            break
        
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            # 범위 내
            if 0<=nr<= n-1 and 0<=nc<=m-1:
                # 방문X 
                if vst[nr][nc] == False:
                    # 벽 없음
                    if maps[nr][nc] == 1:
                        step[nr][nc] = step[cur_r][cur_c] +1
                        vst[nr][nc] = True
                        q.append((nr,nc))
    
    
    if vst[n-1][m-1] == True:
        answer = step[n-1][m-1]
    else:
        answer = -1
    
    
    return answer