import sys
A, B, C = map(int, sys.stdin.readline().split())
lst = []
for _ in range(3):
    f, l = map(int, sys.stdin.readline().split())
    fl =[f, l]
    lst.append(fl)
# 0인 틀 만들기
hlst= []
for i in range(0, max(lst[0][1], lst[1][1], lst[2][1])):
    hlst.append(0)

for j in range(3):
    for i in range(lst[j][0],lst[j][1]):
        if hlst[i] == 2:
            hlst[i] = 3
        elif hlst[i] == 1:
            hlst[i] = 2
        else:
            hlst[i] = 1
dap = 0
for i in range(len(hlst)):
    if hlst[i] == 1:
       dap+=A
    elif hlst[i] == 2:
       dap+=B*2
    elif hlst[i] == 3:
       dap+=C*3
print(dap)

