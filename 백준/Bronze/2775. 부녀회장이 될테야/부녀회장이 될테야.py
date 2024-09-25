import sys
dap = 0
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    lst = list(range(1,n+1))
    tmp = 0
    for i in range(1, k+1):
        lst_sum = []
        tmp = 0
        for j in range(n):

            tmp += lst[j]
            lst_sum.append(tmp)
        lst = lst_sum

    print(lst[-1])