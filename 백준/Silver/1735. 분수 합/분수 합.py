import sys
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

dap =[]
dap.append(a[0]*b[1]+a[1]*b[0])
dap.append(a[1]*b[1])
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

print(int(dap[0]/gcd(dap[0],dap[1])), int(dap[1]/gcd(dap[0],dap[1])))
