# 끝나는 순서 정렬 후 시작 시간 정렬 -> 그리디 하나씩 탐색하기
import sys
n = int(sys.stdin.readline())

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

lst.sort(key = lambda x: (x[1], x[0]))

cont = 1
end = lst[0][1]

for i in range(1,len(lst)):
    if end <= lst[i][0]:
        cont+=1
        end = lst[i][1]


print(cont)