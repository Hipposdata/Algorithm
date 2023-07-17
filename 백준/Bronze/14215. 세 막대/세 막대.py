import sys
lst =list(map(int,sys.stdin.readline().split()))
lst.sort()

tf = True
if lst[2] < lst[0]+lst[1]:
    print(sum(lst))
else:
    mx = lst[2]
    while tf:
        mx-=1
        if mx <lst[0]+lst[1]:
            print(mx+lst[0]+lst[1])
            tf = False