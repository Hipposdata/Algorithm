import sys

n = int(sys.stdin.readline())

lst = [ [] for i in range(n) ]
for i in range(n):
    lst[i].append(sys.stdin.readline().strip())


garo = 0
sero = 0
for j in range(n):
    row = 0
    for q in range(n):
        if lst[j][0][q]== '.':
            row +=1
        if lst[j][0][q]== 'X' or q == n-1:
            if row >=2:
                garo +=1
            row = 0
    col = 0
    for q in range(n):
        if lst[q][0][j]== '.':
            col +=1
        if lst[q][0][j]== 'X' or q == n-1:
            if col >=2:
                sero +=1
            col = 0



print(garo, sero)