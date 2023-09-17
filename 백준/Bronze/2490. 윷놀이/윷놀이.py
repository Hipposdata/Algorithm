import sys

for i in range(3):
    Yutnori = list(map(int,sys.stdin.readline().split()))
    if Yutnori.count(1) == 4:
        print('E')
    elif Yutnori.count(1) == 3:
        print('A')
    elif Yutnori.count(1) == 2:
        print('B')
    elif Yutnori.count(1) == 1:
        print('C')
    else:
        print('D')