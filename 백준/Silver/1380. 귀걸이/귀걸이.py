import sys

dap = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    lst = [0] * n
    name_lst = []
    for i in range(n):
        name = sys.stdin.readline().strip()
        name_lst.append(name)
    for j in range(2*n-1):
        num, alpha = sys.stdin.readline().split()
        lst[int(num)-1]+=1

    for k in range(len(lst)):
        if lst[k] != 2:
            dap.append(name_lst[k])


for l in range(len(dap)):
    print(l+1, dap[l])