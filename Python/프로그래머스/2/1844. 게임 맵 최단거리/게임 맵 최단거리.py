from collections import deque 

def solution(maps):
    answer = 0
    
    col = len(maps[0])
    row = len(maps)

    # 방향 하좌상우
    dr = [1, 0 ,-1,0]
    dc = [0,-1,0,1]
    
    # 방문여부
    vst = [[False] * col for _ in range(row)]
    # 처음시작 -> 방문
    vst[0][0] = True
    
    # 이동 
    step = [[-1]*(col) for _ in range(row)]
    step[0][0] = 1
    
    q = deque()
    q.append((0,0)) # 시작지점
    
    while q:
        cur_r, cur_c = q.popleft()
        
        # 하좌상우 탐색 -> 다음 칸 
        for i in range(4):
            nxt_r = cur_r + dr[i]
            nxt_c = cur_c + dc[i]
            
            #범위내
            if 0<=nxt_r<row and 0<=nxt_c<col:
                # 벽X, 방문X 
                if maps[nxt_r][nxt_c] ==1 and vst[nxt_r][nxt_c] == False:
                    vst[nxt_r][nxt_c] = True
                    step[nxt_r][nxt_c] = step[cur_r][cur_c] + 1
                    q.append((nxt_r, nxt_c))
                    

    answer = step[-1][-1]
    
    return answer