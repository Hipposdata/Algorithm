import sys

a,b = sys.stdin.readline().split()

a= map(int,list(a))
b= map(int,list(b))
print(sum(a) * sum(b))
# for문으로 각자리수 돌면서 곱하면 시간초과 발생 / 더한후 곱허기