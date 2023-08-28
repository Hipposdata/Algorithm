import sys
n =int(sys.stdin.readline())

for i in range(n,0,-1):
    i = list(str(i))
    if len(i) == i.count('4') + i.count('7'):
        print("".join(i))
        break