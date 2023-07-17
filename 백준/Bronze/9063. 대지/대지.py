import sys
N = int(sys.stdin.readline())

xlst =[]
ylst =[]
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    xlst.append(x)
    ylst.append(y)

if N == 1:
    print(0)
else :
    print((max(xlst)-min(xlst))*(max(ylst)-min(ylst)))
