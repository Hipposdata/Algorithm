import sys

n = int(sys.stdin.readline())
customer = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(1, len(customer)):
    if customer[i] in  customer[:i]:
        cnt +=1

print(cnt)

