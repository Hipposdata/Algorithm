import sys
# 입력한 값보다 큰수의 개수를 세면 됨
n,sc,p = map(int,sys.stdin.readline().split())
if n > 0:
    lst = list(map(int,sys.stdin.readline().split()))
    rank = 1
    for i in lst:
        if i > sc:
            rank +=1
        else:
            break

    if n == p and lst[-1] >= sc:
        print(-1)
    else:
        print(rank)
else:
    print(1)

