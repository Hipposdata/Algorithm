import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a = input()
    lst.append(a)
lst = list(set(lst))  #중복제거

lst.sort()
lst.sort(key= len)

for i in range(len(lst)):
    print(lst[i])