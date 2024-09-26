import sys
alpha = {chr(i): i - 96 for i in range(97, 123)}

n = int(sys.stdin.readline())
ch = sys.stdin.readline()

dap = 0
for i in range(n):
    dap += alpha[ch[i]] *(31**i)
print(dap)
