import sys
a = list(map(int,sys.stdin.readline().split()))

if a == list(range(1, 9)):
    print("ascending")
elif a == list(range(1, 9)[::-1]):
    print("descending")
else:
    print("mixed")