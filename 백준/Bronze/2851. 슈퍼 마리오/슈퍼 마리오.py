

lst = []
for i in range(10):
    a = int(input())
    lst.append(a)
dap_1 = 0
for i in range(10):
    dap_1+=lst[i]


dap = 0
for i in range(10):
    dap += lst[i]
    jeon = dap - lst[i]
    if dap>=100:
        if abs(100-dap) < abs(100-jeon):
            print(dap)
            break
        if abs(100-dap) > abs(100-jeon):
            print(jeon)
            break
        if abs(100-dap) == abs(100-jeon):
            print(dap)
            break
    if dap_1<100:
        print(dap_1)
        break
