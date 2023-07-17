import sys

tf = True
while tf:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        tf = False
    else:
        if a+b <=c or a+c <=b or b+c<=a:
            print("Invalid")
        else:
            if a==b==c and a !=0:
                print("Equilateral")
            if a==b != c or a==c != b or b==c !=a:
                print("Isosceles")
            if a!=b and a!=c and b !=c:
                print("Scalene")
