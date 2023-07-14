import sys
C= int(sys.stdin.readline())
lst = []
for i in range(C):
    gap = list(map(int, sys.stdin.readline().split()))
    min = sum(gap[1:])/gap[0]
    count = 0
    hap = 0
    for j in range(1,len(gap)):
        if min < gap[j]:
            count +=1
            hap = (count/gap[0])*100
    print(str("{:.3f}".format(round(hap,3)))+"%")