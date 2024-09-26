import sys


while True:
    iprek = list(sys.stdin.readline().rstrip())
    stack = []
    dap = 'yes'
    if iprek == ['.']:
        break

    for i in iprek:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    dap = 'no'
                    break
            else:
                dap = 'no'
                break
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    dap = 'no'
                    break
            else:
                dap = 'no'
                break
    if stack:
        dap = 'no'
    print(dap)