import sys

dap = 0
lst = []
for i in range(4):
    getout, getin = map(int,sys.stdin.readline().split())
    dap += getin - getout
    lst.append(dap)

print(max(lst))