import sys
tf = True
while tf:
    a , b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        tf = False
    if a< b:
        if b%a ==0:
            print("factor")
        else:
            print("neither")
    if a>b:
        if a%b == 0:
            print("multiple")
        else:
            print("neither")