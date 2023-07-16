import sys

N = int(input())

lst = []
for i in range(N):
    w, h = map(int,sys.stdin.readline().split())
    a=[w,h]
    lst.append(a)

t = []
for i in range(N):
    t.append(1)

dap = []
for i in range(N):
    count = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            count +=1
            t[i] = count


for i in range(N):
    print(t[i], end=" ")
