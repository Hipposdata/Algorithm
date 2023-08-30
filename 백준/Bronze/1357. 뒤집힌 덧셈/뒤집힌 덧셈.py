import sys

x ,y = map(int,sys.stdin.readline().split())

x = int(''.join(reversed(str(x))))
y = int(''.join(reversed(str(y))))
dap = x+y
dap = int(''.join(reversed(str(dap))))

print(dap)