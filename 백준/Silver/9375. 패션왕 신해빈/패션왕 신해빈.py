import sys
t = int(sys.stdin.readline())


for _ in range(t):
    n = int(sys.stdin.readline().strip())

    dic = {} # 목록 명
    idx = 0
    lst = [[] for i in range(n)]
    dap = 1
    for _ in range(n):
        a, b = sys.stdin.readline().strip().split()
        if b not in dic:
            dic[b] = idx
            idx +=1


        lst[dic[b]].append(a)
    for j in lst:
        dap *= len(j)+1
    print(dap -1)