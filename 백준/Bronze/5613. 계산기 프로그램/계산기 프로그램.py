import sys

tmp = 0
lst = []
opt = ['+', '-', '*', '/']
num = []
while True:
    n = sys.stdin.readline().strip()
    if n in opt:
        lst.append(n)
    elif n == '=':
        lst.append(n)
        break
    else:
        num.append(int(n))
num_re = list(reversed(num))
tmp = num_re.pop()

dap = 0
for i in lst:
    if num_re:
        tmp2 = num_re.pop()
    if i == '=':
        print(tmp)
    elif i == '/':
        tmp = int(tmp / tmp2)
    elif i == '+':
        tmp +=  tmp2
    elif i == '-':
        tmp -=  tmp2
    elif i == '*':
        tmp *=  tmp2