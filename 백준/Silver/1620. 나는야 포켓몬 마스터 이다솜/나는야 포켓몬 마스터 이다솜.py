import sys
n, m = map(int,sys.stdin.readline().split())

dic = {}
for i in range(1,n+1):
    dic[sys.stdin.readline().strip()] = i

dic_rev = {v:k for k,v in dic.items()}
# 키 밸류 바꿔주기
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit() :
        print(dic_rev[int(q)])
    else :
        print(dic[q])