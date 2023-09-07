import sys

n = sys.stdin.readline()[:-1]

if len(n) == 1:
    n = n + '0'
tmp = n[1] + (str(int(n[0])+int(n[-1])))[-1]

cnt =1
tf = True

while tf:
    if n == tmp:
        print(cnt)
        tf = False
    else:
        if len(tmp) == 1:
            tmp = tmp + '0'
        tmp = tmp[1] + (str(int(tmp[0])+int(tmp[-1])))[-1]
        cnt +=1