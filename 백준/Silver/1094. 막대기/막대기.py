import sys
stick = [64,32,16,8,4,2,1]
x = int(sys.stdin.readline())
cnt = 0
for i in stick:
    if x >= i:
        x -= i
        cnt += 1
        if x == 0:
            print(cnt)