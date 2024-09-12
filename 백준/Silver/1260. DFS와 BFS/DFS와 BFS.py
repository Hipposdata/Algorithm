
import sys
sys.setrecursionlimit(1000)
n, m, start = map(int, sys.stdin.readline().split())
vst = [False] * (n+1) # 방문기록

ar = [[]for _ in range(n+1)] # 인접 리스트


for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    ar[s].append(e) # 양쪽 엣지 더하기
    ar[e].append(s)

for i in range(n+1):
    ar[i].sort() # 작은 노드부터 방문하기위해 정렬


def DFS(v):
    print(v, end=' ')
    vst[v] = True
    for i in ar[v]:
        if not vst[i]:
            DFS(i)

from collections import deque

def BFS(v):
    queue = deque()
    queue.append(v)
    vst[v] = True
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for i in ar[node]:
            if not vst[i]:
                vst[i] = True
                queue.append(i)



DFS(start)
print()
vst = [False] * (n+1) # 방문기록초기화
BFS(start)