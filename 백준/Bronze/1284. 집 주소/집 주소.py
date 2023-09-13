import sys

tf = True
while tf:
    num = list(sys.stdin.readline()[:-1])
    if num[0] =='0' and len(num) == 1:
        tf = False
    else:
        dap = 0
        for i in num:
            if i == '1':
                dap +=2
            elif i == '2':
                dap +=3
            elif i =='0':
                dap += 4
            else :
                dap +=3
        print(len(num)+1+dap)
