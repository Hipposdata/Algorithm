import sys

lst= [1,1,1]

def suyeal(n):
    while len(lst) < n:
        lst.append(lst[-3] + lst[-2])
    return lst[n - 1]


t = int(sys.stdin.readline())
for _ in range(t):
    print(suyeal(int(sys.stdin.readline().strip())))