import sys

n, k = map(int,sys.stdin.readline().split())

lst = []
for _ in range(n):
    a,b,c,d = map(int,sys.stdin.readline().split())
    lst.append((a,b,c,d))

lst.sort(key=lambda x: (x[1],x[2],x[3]),reverse = True)

target = 0
# 등수 세기
for i in range(0,len(lst)):
    if lst[i][0] == k:
        target += 1
        break
    else:
        target+=1

# 같은거 개수 찾기
rank = 0
for j in range(0,len(lst)):
    if lst[target-1][1:] == lst[j][1:]:
        print(rank +1)
        break
    else:
        rank +=1

