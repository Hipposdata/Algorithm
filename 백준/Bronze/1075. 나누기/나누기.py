import sys

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())
n = list(str(n))
n[-2:] = ["0","0"]
n = int("".join(n))

tf= True
while tf:

    if n % f ==0:
        print(str(n)[-2:])
        tf = False
    n +=1