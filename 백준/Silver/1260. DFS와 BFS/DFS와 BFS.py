#####################dfs bfs 

import sys
from collections import deque

n ,m ,v = map(int, sys.stdin.readline().split()) # n정점/m간선/v시작점
graph = []
for i in range(n+1): # 정점 만들기 / 인덱스번호와 정점번호 일치위해 0~n+1까지 만듦
    graph.append([])

for i in range(m): # 각 정점에 인접정점번호 넣기
    v1, v2 = map(int,sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort()
# 순서보정 위해 오름차순 정렬


# bfs 함수 작성
def bfs(start):
    queue = deque() # 빈 덱 만들기
    visited=[]
    for i in range(n+1):   # for [0 for _ in range(n+1)]
        visited.append(0)  # 방문목록에 0 넣음 방문시1 미방문 0
    queue.append(start) #  큐에 시작 정점번호 표시
    visited[start] = 1     # [0, 1, 0, 0, 0] # 시작정점 방문표시

    while len(queue) > 0: # queue에 남아있는게 없을때까지 실행
        curr = queue[0] # queue의 첫번째 수 확인 / 시작번호 확인
        print(curr, end=' ')
        for nxt in graph[curr]: # 시작 정점(인덱스)에 인접한 정점번호 하나씩 할당
            if visited[nxt] == 0: # 아직 방문 안한 정점만 가야함
                visited[nxt] = 1 # 방문했다고 표시하기
                queue.append(nxt) # queue에 넣기
        queue.popleft() # 선입선출

# dfs 함수 작성
dfs_sol = 0
bfs_sol = 0

visit = []
for i in range(n+1):   # for [0 for _ in range(n+1)]
    visit.append(0) 
visit[v] = 1

def dfs(curr):
    print(curr, end=' ')
    for nxt in graph[curr]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            dfs(nxt) # 재귀함수 적용 
dfs(v)
print()
bfs(v)
