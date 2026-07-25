import heapq

def solution(n, road, k):
    graph = [[] for _ in range(n+1)]
    
    for a,b,c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 각 마을까지의 거리 / 각 인덱스가 노드 
    dst = [float("inf")] * (n+1)
    # 1번에서 시작하므로 0
    dst[1] = 0
    
    # 탐색할 노드 대기열 / 거리(가중치), 노드번호
    # 가중치부터 저장해야함 -> 우선순위큐 위해 
    q = []
    # 1번노드까지는 0거리 
    q.append((0,1))
    
    while q:
        cur_dst, cur = heapq.heappop(q)
        
        if cur_dst > dst[cur]:
            continue 
            
        # 해당 노드와 연결된 노드 순회 
        for nxt, c in graph[cur]:
            new_dst = cur_dst + c
            
            # 노드 최단거리 업데이트 
            if new_dst < dst[nxt]:
                dst[nxt] = new_dst
                heapq.heappush(q, (new_dst, nxt))
    answer = 0
    for i in dst[1:]:
        if i <= k:
            answer +=1
    
    return answer