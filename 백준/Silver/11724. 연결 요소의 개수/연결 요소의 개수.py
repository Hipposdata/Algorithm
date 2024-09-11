
import sys
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)] # 인접리스트
vst = [False] * (n+1) # 방문기록

def DFS(v):
    vst[v] = True # 현재 노드 방문 기록
    for i in a[v]:
        if not vst[i]:
            DFS(i) # 재귀함수형태로 미방문 연결노드 DFS실행

for _ in range(m): # 엣지 반복
    s, e = map(int, sys.stdin.readline().split())
    a[s].append(e)
    a[e].append(s)

cont = 0

# 탐색
for i in range(1,n+1):
    if not vst[i]:
        cont +=1
        DFS(i)

print(cont)