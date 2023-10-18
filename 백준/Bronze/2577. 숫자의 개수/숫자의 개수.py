import sys

a =int(sys.stdin.readline())
b =int(sys.stdin.readline())
c =int(sys.stdin.readline())

hap =list(map(int,str(a * b * c)))
for i in range(0,10):
    print(hap.count(i))