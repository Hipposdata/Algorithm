from collections import Counter
import sys
N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    a = int(sys.stdin.readline())
    lst.append(a)

print(round(sum(lst) / len(lst))) # 평균 ㅇ
print(sorted(lst)[len(lst)//2])  # 중앙값 o
c = Counter(sorted(lst)).most_common(2) # 최빈값 o
if len(lst) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])
print(sorted(lst)[-1]-sorted(lst)[0]) # 범위 0