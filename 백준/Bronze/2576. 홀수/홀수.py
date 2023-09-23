import sys

odd = []
for i in range(7):
    num = int(sys.stdin.readline())
    if num % 2 != 0:
        odd.append(num)
if len(odd) ==0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
