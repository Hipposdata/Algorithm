import sys

t = int(sys.stdin.readline())
for i in range(t):
   num = list(sys.stdin.readline()[:-1])
   print(int(num[0]) + int(num[-1]))