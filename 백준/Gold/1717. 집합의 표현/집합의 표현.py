import sys

n,m = map(int, sys.stdin.readline().split())
lst = [i for i in range(n+1)] #각 노드의 부모노드/ 인덱스: 노드번호 / 값: 부모노드

def union(a,b): # 노드 합치기
    a = find(a)
    b = find(b)
    if a != b:
        lst[b] = a

def find(a): # 그래프의 부모노드 찾기
    if a == lst[a]:
        return a
    else:
        lst[a] = find(lst[a])
        return lst[a]

def same(a,b):
    # find 연산후 최종 부모노드 값 표시
    a = find(a)
    b = find(b)

    if lst[a] == lst[b]:
        return True
    else:
        return False

for _ in range(m):
    num ,a,b =  map(int, sys.stdin.readline().split())
    if num == 0:
        union(a,b)
    else:
        if same(a,b):
            print("YES")
        else:
            print("NO")



