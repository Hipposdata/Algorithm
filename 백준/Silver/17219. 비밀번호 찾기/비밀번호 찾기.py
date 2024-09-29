import sys
n, m = map(int,sys.stdin.readline().split())

dic ={}
for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    dic[a] = b

for _ in range(m):
    password = sys.stdin.readline().strip()
    print(dic[password])