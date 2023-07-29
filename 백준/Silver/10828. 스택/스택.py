import sys

N = int(sys.stdin.readline())
dap = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        dap.append(command[1])
    elif command[0] == 'pop':
        if len(dap) ==0:
            print(-1)
        else:
            print(dap[-1])
            dap.pop()
    elif command[0] == 'size':
        print(len(dap))
    elif command[0] == 'empty':
        if len(dap) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(dap) == 0:
            print(-1)
        else:
            print(dap[-1])