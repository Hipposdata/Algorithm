import sys

n = int(sys.stdin.readline())

chang = 100
seong = 100
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a>b:
        seong -= a
    elif a<b:
        chang -= b

print(chang)
print(seong)