import sys

n = int(sys.stdin.readline())

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()
cont = 0
for i in range(n):
    if s1[i] != s2[i]:
        cont +=1

print(cont)