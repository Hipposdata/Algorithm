import sys
iprek = list(sys.stdin.readline())

memo = 0
stack = []
dap = 0
for i in iprek:
    if i == '.'or i == iprek[-1]:

        if memo %4 == 0:
            stack.append('AAAA' * (memo //4))
        elif memo % 2 == 0:
            if memo >=6:
                stack.append('AAAA' * (memo // 4))
                memo = memo % 4
                stack.append('BB' * (memo // 2))
            else: # memo <6
                stack.append('BB' * (memo // 2))
        elif memo == 0:
            pass
        else:
            dap = -1


        if i == '.':
            stack.append('.')
        memo = 0
    if i == 'X':
        memo +=1

if dap ==  -1:
    print(-1)
else:
    for j in stack:
        print(j,end='')
