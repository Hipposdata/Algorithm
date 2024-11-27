import sys
import heapq
v,e = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())

# 인접리스트 생성
grp = [[] for i in range(v+1)]
for _ in range(e):
    u,v2,w =  map(int,sys.stdin.readline().split())
    grp[u].append((v2,w))

# 거리기록
dst = [sys.maxsize] * (v+1) # 거리기록 / 초기 임의 최대값상수
dst[k] = 0 # 시작지점 거리 0
vst = [False] * (v+1)

q = [] # 우선순위 큐 리스트 생성
heapq.heappush(q,(0,k))# 초기거리 ,시작지점을 큐에 삽입 / 최단거리 기준으로 최소값 뽑아야 하기 때문

while len(q) >0:
    distance ,node = heapq.heappop(q)
    if vst[node] : # 방문한적 있다면 넘어감
        continue
    vst[node] = True # 노드 방문처리
    for i in grp[node]: # 인접노드들 계산
        next_node = i[0]
        weight = i[1]
        if dst[next_node] > distance + weight: #최소거리 업데이트
            dst[next_node] = distance + weight
            heapq.heappush(q,(dst[next_node],next_node)) # 큐에 노드 삽입

for i in range(1,len(dst)):
    if vst[i]:
        print(dst[i])
    else:
        print("INF")