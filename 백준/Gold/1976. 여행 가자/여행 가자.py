import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n+1)]
def find(a): #재귀적을 타고올라가서 해당노드의 부모노드 출력, 경로압축효과
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a] #경로압축효과

def union(a,b): #재귀적으로 타고 올라가서 최종 노드의 값과 인덱스 값을 일치시킴
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

city = [[0 for col in range(n+1)] for row in range(n+1)]

for i in range(1, n+1):
    city[i] = [0]+list(map(int, sys.stdin.readline().split()))

# 여행경로 저장
route = list(map(int,sys.stdin.readline().split()))

for row in range(1, len(city)):
    for col in range(1, len(city)):
        if city[row][col] == 1:
            union(row, col)

# print(parent)
check = find(route[0])
dap = "YES"
for i in route[1:]:
    if check != find(i):
        dap = "NO"
        break

print(dap)
# 부모노드가 동일한경우 -> 여행가능 (같은 그래프내에 존재함)