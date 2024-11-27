import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

lst = [0] * 5
u = s.count('u')
o = s.count('o')
s1 = s.count('s')
p = s.count('p')
c = s.count('c')

print(min(u,o,s1,p,c))