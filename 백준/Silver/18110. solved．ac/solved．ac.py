import sys
lst = []
n = int(sys.stdin.readline())


def ban(n):
    if n - int(n) < 0.5:
        return int(n)
    else:
        return int(n) + 1

if n == 0:
    print(0)
else:
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.sort()
    num = ban(n *0.15)

    print(ban(sum(lst[num:  n -  num])/len(lst[num:  n -  num])))