import sys
E, S, M = map(int, sys.stdin.readline().split())
i ,j ,k =0 ,0 ,0
sum = 0
while True:
    i+=1
    j+=1
    k+=1
    sum+=1
    if i == 16:
        i=1
    if j == 29:
        j=1
    if k == 20:
        k=1
    if i == E and j == S and k ==M:
        print(sum)
        break