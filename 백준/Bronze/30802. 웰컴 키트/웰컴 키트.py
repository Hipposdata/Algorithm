import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

cont = 0
for i in lst:
    if i == 0:
        pass
    elif i%t == 0:
        cont += (i//t)
    else: # i%t != 0
        cont += i//t +1


print(cont)
print(n //p, n % p)