#행렬곱
import sys
A = list(map(int, sys.stdin.readline().split()))
alst = []
for i in range(A[0]):
    a = list(map(int, sys.stdin.readline().split()))
    alst.append(a)
B = list(map(int, sys.stdin.readline().split()))
blst = []
for i in range(B[0]):
    b = list(map(int, sys.stdin.readline().split()))
    blst.append(b)
#
# print(alst)
# print(blst)
# print(A)
# print(B)

hap = []
dap = []
# for i in range(A[0]):
#     a = []
#     for j in range(B[1]):
#         a.append(0)
#     dap.append(a)

dap = [ [0 for _ in range(B[1])] for _ in range(A[0]) ]
# print(dap)
for i in range(A[0]):
    for k in range(B[1]):
        for m in range(A[1]):
            # print(i,m)
            # print(m,k)
            # print('--------')
            dap[i][k] += alst[i][m] * blst[m][k]

for i in dap :
    print(*i)