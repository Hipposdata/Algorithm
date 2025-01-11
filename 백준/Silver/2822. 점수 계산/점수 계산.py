import sys

lst = []
for i in range(1,8+1):
    score = int(sys.stdin.readline())
    lst.append((i,score))

lst.sort(key = lambda x: x[1], reverse = True)

hap = 0
ord = []
for j in lst[:5]:
    hap +=j[1]
    ord.append(j[0])
print(hap)
ord.sort()
for k in ord:
    print(k, end = ' ')