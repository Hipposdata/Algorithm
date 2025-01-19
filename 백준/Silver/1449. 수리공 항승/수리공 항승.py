import sys

n, l = map(int,sys.stdin.readline().split())


lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

cont = 1
record = lst[0] - 0.5
for i in range(1, len(lst)):
    if record  + l < lst[i] :
        record = lst[i] - 0.5
        cont +=1

print(cont)
