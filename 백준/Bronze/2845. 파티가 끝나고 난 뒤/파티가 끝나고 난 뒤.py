import sys

l,p = map(int,sys.stdin.readline().split())

num = l * p


gisa = list(map(int,sys.stdin.readline().split()))

print(gisa[0]-num,gisa[1]-num,gisa[2]-num,gisa[3]-num,gisa[4]-num)