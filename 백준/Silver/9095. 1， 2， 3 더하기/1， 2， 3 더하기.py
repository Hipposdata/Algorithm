import sys
t = int(sys.stdin.readline())

def fac(a):
    dap = 1
    for i in range(1,a+1):
        dap *= i
    return dap

def sett(a):
    for i in a:
        if i != 0:
            return i


for _ in range(t):
    n = int(sys.stdin.readline().strip())
    dap = 0
    lst = []
    for i in range(0,3+1):
        for j in range(0,5+1):
            for k in range(0,11+1):
                if 3*i + 2*j + k == n:
                    lst.append([i,j,k])

    for q in lst:
        nanugi = 1
        for p in q:
            nanugi *= fac(p)
        dap += (fac(sum(q))) / nanugi
    print(int(dap))