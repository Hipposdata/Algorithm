import sys

n = int(sys.stdin.readline())

numlst = []
for i in range(n):
    num = int(sys.stdin.readline())
    numlst.append(num)
if numlst[1] - numlst[0] == numlst[2] - numlst[1]:
    print(numlst[-1] + (numlst[1] - numlst[0]) )
else:
    print(int(numlst[-1] * (numlst[1] / numlst[0])))