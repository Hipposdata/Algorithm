# 최단거리 bfs
from collections import deque

def solution(maps):
    answer = 0
    
    # 행렬
    col = len(maps[0])
    row = len(maps)
    
    # 방향 하좌상우
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    
    # 방문여부
    vst = [[False] * (col) for _ in range(row)]
    vst[0][0] = True
    
    # 이동기록
    step = [[-1] * (col) for _ in range(row)]
    step[0][0] = 1

    q = deque()
    q.append((0,0))
    
    while q:
        cur_r, cur_c = q.popleft()
        
        
        for i in range(4):
            nxt_r = cur_r + dr[i]
            nxt_c = cur_c + dc[i]
            
            # 범위 내 
            if 0<= nxt_r < row and 0<= nxt_c < col:
                # 벽없음, 방문 X 
                if maps[nxt_r][nxt_c] == 1 and vst[nxt_r][nxt_c] == False:
                    vst[nxt_r][nxt_c] = True
                    step[nxt_r][nxt_c] = step[cur_r][cur_c] +1
                    q.append((nxt_r, nxt_c))
                    
                    
    if step[-1][-1] == -1:
        answer = -1
    else:
        answer = step[-1][-1]
                    
    
    return answer