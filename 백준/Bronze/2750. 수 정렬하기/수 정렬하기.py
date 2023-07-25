n = int(input())

lst =[]
for i in range(n):
    a =int(input())
    lst.append(a)

for j in range(n-1):
    mn = lst[j]
    for k in range(j+1,n):
        if mn> lst[k]:
            mn = lst[k]
            lst[j], lst[k] = lst[k], lst[j]

for q in range(len(lst)):
    print(lst[q])
