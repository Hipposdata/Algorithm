import sys

dap = []
for i in range(1,5+1):
    name = sys.stdin.readline().strip()
    if 'FBI' in name:
        dap.append(i)

if dap:
    for j in dap:
        print(j, end =' ')
else:
    print("HE GOT AWAY!")