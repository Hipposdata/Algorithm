def d(n):
    a = sum(list(map(int, list(str(n))))) + n
    return a
n = 0
dap = []
while  n<=10000 :
    n+=1
    if d(n) <=10000:
        dap.append(d(n))
dap = list(set(dap))
for i in range(1,10001):
    if i not in dap:
        print(i)