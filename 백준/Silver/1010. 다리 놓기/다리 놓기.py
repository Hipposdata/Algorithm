import sys
T = int(sys.stdin.readline())

def fac(T):
    if T ==0:
        return 1
    return T* fac(T-1)

for i in range(T):
    N, M = map(int,sys.stdin.readline().split())
    print(int(fac(M)/(fac(M-N)*fac(N))))