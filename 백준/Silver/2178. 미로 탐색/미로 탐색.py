import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())

al = [[0]*m for _ in range(n)] # 인접리스트 빈틀 만들기
vst = [[False] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
# dx[0] = 0, dy[0] = 1 : 오른쪽으로 이동 (→)
# dx[1] = 1, dy[1] = 0 : 아래쪽으로 이동 (↓)
# dx[2] = 0, dy[2] = -1 : 왼쪽으로 이동 (←)
# dx[3] = -1, dy[3] = 0 : 위쪽으로 이동 (↑)


# 빈 인접리스트에 요소 채우기
for i in range(n):
    num = list(sys.stdin.readline())
    for j in range(m):
        al[i][j] = int(num[j])

from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    vst[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4): # 4방향 이동
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>=0 and y>=0 and x<n and y<m: # 미로 범위 이내
                if al[x][y] !=0 and not vst[x][y]: # 방문아직 안했거나 방문가능한곳
                    vst[x][y] = True
                    al[x][y] = al[now[0]][now[1]] +1
                    queue.append((x,y))

bfs(0,0)

# print(al)
# print(vst)
print(al[n - 1][m - 1])
