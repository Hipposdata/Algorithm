import sys

dap = []
for i in range(5):
    num = int(sys.stdin.readline())
    dap.append(num)

print(sum(dap))