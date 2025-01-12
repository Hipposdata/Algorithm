import sys

n, k = map(int,sys.stdin.readline().split())

lst = []
for _ in range(n):
    a,b,c,d = map(int,sys.stdin.readline().split())
    lst.append((a,b,c,d))

lst.sort(key=lambda x: (x[1],x[2],x[3]),reverse = True)

rank =1
# 등수 세기
for i in range(0,len(lst)):
    if lst[i][0] == k:
        break
    else:
        rank+=1

# 같은거 개수 찾기
same = 0
for j in range(0,len(lst)):
    if lst[rank-1] == lst[j]:
        same +=1

print(rank - same)

