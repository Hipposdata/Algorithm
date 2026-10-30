# 최단거리 bfs
from collections import deque


def solution(maps):
    answer = 0
    # 방문여부 기록
    row = len(maps)
    col = len(maps[0])
    
    vst = [[False] * col for _ in range(row)]
    # 시작위치는 방문처리
    vst[0][0] == True
    
    # 이동 개수 지도에 표시
    step = [[0] * col for _ in range(row)]
    step[0][0] = 1
    
    
    # 방향 하좌상우
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    
    q = deque()
    # 시작지점 좌표 인덱스 
    q.append((0,0))
    
    while q:
        cur_r, cur_c = q.popleft()
        
        # 다음좌표 계산
        for i in range(4):
            n_r = cur_r + dr[i]
            n_c = cur_c + dc[i]
            
            # 범위내
            if 0<=n_r<row and 0<=n_c<col:
                # 방문 X
                if vst[n_r][n_c] == False:
                    # 벽X
                    if maps[n_r][n_c] != 0:
                        vst[n_r][n_c] = True
                        step[n_r][n_c] = step[cur_r][cur_c]  +1
                        q.append((n_r, n_c))
                        
    if step[-1][-1] == 0:
        answer = -1
    else:
        answer = step[-1][-1]
    return answer