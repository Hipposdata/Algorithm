import sys

n = int(sys.stdin.readline())
firlst = []
for i in range(n):
    name = sys.stdin.readline()[0]
    firlst.append(name)

dap = []
for i in set(firlst):
    if firlst.count(i) >= 5:
       dap.append(i)
if len(dap) != 0:
    print("".join(sorted(dap)))
else:
    print('PREDAJA')