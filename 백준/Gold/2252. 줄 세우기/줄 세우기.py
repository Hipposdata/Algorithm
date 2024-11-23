import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

st = [[] for _ in range(n+1)] # 학생들 인접 리스트
indegree = [0] * (n+1) # 진입차수 / 인덱스 -> 노드 / 값 -> 진입차수

for _ in range(m):
    a, b= map(int,sys.stdin.readline().split())
    st[a].append(b)
    indegree[b] +=1 # 진입차수 증가

queue = deque()
for i in range(1,len(indegree)): # 진입차수 0인노드 큐에추가
    if indegree[i] == 0:
        queue.append(i)

while queue: # 위상정렬 수행
    idx = queue.popleft() # 큐에서 원소 꺼내기
    print(idx, end = ' ')
    for i in st[idx]: # 연결된 간선 진입차수 1씩 뺌
        indegree[i] -=1
        if indegree[i] == 0: # 진입차수 0일시 다시 추가
            queue.append(i)