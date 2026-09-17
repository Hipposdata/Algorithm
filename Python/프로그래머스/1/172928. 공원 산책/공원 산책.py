def solution(park, routes):
    answer = []
    
    col = len(park)
    row = len(park[0])
    
    #시작점 찾기 
    for r_idx, p in enumerate(park):
        for c_idx, p1 in enumerate(p):            
            if p1 == 'S':
                cur = (r_idx, c_idx)
            
    for r in routes:
        can_move = True
        # 이동횟수 
        for i in range(1, int(r[2:])+1):
            if r[0] == 'N':
                nxt = (cur[0] - i,cur[1])
            elif r[0] == 'S':
                nxt = (cur[0] +i,cur[1])
            elif r[0] == 'W':
                nxt = (cur[0], cur[1] - i)
            elif r[0] == 'E':
                nxt = (cur[0] ,cur[1]+ i)
            # 공원내부
            if 0<=nxt[0]<col and 0<= nxt[1] < row:
                # 장애물 여부
                if park[nxt[0]][nxt[1]] == 'X':
                    can_move = False
                    break
            else:
                can_move = False
                break
        if  can_move:
            cur = nxt

    return cur


