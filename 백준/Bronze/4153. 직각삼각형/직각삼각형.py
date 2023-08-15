import sys

tf = True
while tf :
    a,b,c = map(int,sys.stdin.readline().split())
    if a+b+c ==0:
        tf= False
    else:
        if a**2 == b**2+c**2 or b**2==c**2+a**2 or c**2==a**2+b**2:
            print("right")
        else:
            print("wrong")