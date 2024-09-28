import sys
n, m = map(int, sys.stdin.readline().split())

n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(sys.stdin.readline().strip())
for _ in range(m):
    m_set.add(sys.stdin.readline().strip())

tmp = list(n_set & m_set)
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)