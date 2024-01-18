import sys
n = int(sys.stdin.readline())


for i in range(n):
    H, W, N = map(int,sys.stdin.readline().split())
    floor =  N % H
    room = (N // H) + 1
    if floor == 0:
        floor = H
        room -= 1
    if room <=9 :
        room = str(0) + str(room)
    print(str(floor) + str(room))