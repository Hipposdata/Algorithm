import sys

for i in range(3):
    hap = 0
    n = int(sys.stdin.readline())
    for i in range(n):
        num = int(sys.stdin.readline())
        hap += num
    if hap == 0:
        print("0")
    elif hap > 0:
        print("+")
    else:
        print("-")