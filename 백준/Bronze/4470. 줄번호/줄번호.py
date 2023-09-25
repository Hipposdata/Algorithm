import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    iprek = sys.stdin.readline().rstrip()
    print(f'{i}. {iprek}')