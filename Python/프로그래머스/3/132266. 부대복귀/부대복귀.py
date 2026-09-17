# 최단거리 BFS 
# 목적지 기준 각 위치 도달거리 계산 -> dst 저장 

from collections import deque 
def solution(n, roads, sources, destination):
    
    # 인접 리스트
    graph = [[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)     
    
    # 각 노드까지의 최단거리 저장 
    dst = [-1] * (n+1)
    dst[destination] = 0
        
    q = deque()
    q.append(destination)

    while q:
        cur = q.popleft()
        
        # 모든 노드 순회 -> 해당 노드와 연결된 노드만 순회
        for nxt in graph[cur]:
            # 두 노드 연결되어있거나 / 아직 방문 X 
            if  dst[nxt] == -1:
                dst[nxt] = dst[cur] +1
                q.append(nxt)
                
            
    
    return [dst[i] for i in sources]