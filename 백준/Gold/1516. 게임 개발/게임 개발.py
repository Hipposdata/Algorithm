import sys
from collections import deque

n = int(sys.stdin.readline()) # 건물수

tower = [[] for _ in range(n+1)] # 건물 인접리스트
hour = [0] *(n+1) # 건물생산시간

for i in range(1,n+1):
    lst = list(map(int, sys.stdin.readline().split()))
    if len(lst) == 2:
        hour[i] = lst[0]
    else:
        hour[i] = lst[0]
        for j in range(1, len(lst)-1): # 마지막 -1제외 반복
            tower[lst[j]].append(i)

indegree = [0] *(n+1) # 진입차수
for i in range(1,len(tower)):
    if tower[i]:
        for j in tower[i]:
            indegree[j] +=1

queue = deque()
for i in range(1,len(indegree)): # 진입차수 0인 노드 큐에 삽입
    if indegree[i] == 0:
        queue.append(i)


dap = hour.copy()

while queue:
    node = queue.popleft()
    for i in tower[node]: # 인접노드
        indegree[i] -=1
        dap[i] = max(dap[i], (hour[i]+dap[node])) #
        if indegree[i] ==0:
            queue.append(i)

for i in dap[1:]:
    print(i)
