import sys

al=[]
bl=[]

for i in range(3):
    a, b = map(int,sys.stdin.readline().split())
    al.append(a)
    bl.append(b)

uq_al = list(set(al))
uq_bl = list(set(bl))

dap = [0,0]
for i in range(2):
    if al.count(uq_al[i]) == 1:
        dap[0] = uq_al[i]
for i in range(2):
    if bl.count(uq_bl[i]) == 1:
        dap[1] = uq_bl[i]

for i in range(2):
    print(dap[i], end=" ")