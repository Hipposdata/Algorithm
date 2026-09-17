# 가장 짧은 -> bfs 

from collections import deque


def solution(begin, target, words):
    answer = 0
    
    # 큐 -> 현재단어, 방문횟수
    q = deque()
    q.append((begin,0))
    step = 0
    vst = []
    vst.append(begin)

    while q:
        cur, step = q.popleft()
        if cur == target:
            break
        
        for i in words:
            cnt = 0
            # 횟수 확인
            for j in range(len(cur)):
                if i[j] != cur[j]:
                    cnt+=1
            if cnt == 1 and i not in vst:
                nw = i
                vst.append(nw)
                q.append((nw, step+1))
                
    if target == cur:
        answer = step
    else:
        answer = 0
    
    return answer