import sys
N = int(sys.stdin.readline())
lst = []
insu = N
tf = True
for i in range(2,N+1):
    while True:
        if insu % i==0:  #인수 하나씩 저장
            lst.append(i)
            insu = insu / i
        else:
            break

for i in range(len(lst)):
    print(lst[i])