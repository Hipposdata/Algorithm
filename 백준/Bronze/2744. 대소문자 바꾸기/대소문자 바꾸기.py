import sys

lst = list(sys.stdin.readline())

dap = []
for i in lst:
    if i.isupper():
        dap.append(i.lower())
    else:
        dap.append(i.upper())


for j in dap:
    print(j, end = '')