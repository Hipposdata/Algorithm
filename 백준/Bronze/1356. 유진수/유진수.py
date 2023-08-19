N =input()

def g(N):
    gap = 1
    for i in N:
        gap *=i
    return gap
lst1= []
lst2= []
for i in range(1,len(N)):
    lst1.append(list(map(int,N[-i:])))

for i in range(len(N)-1):
    a = list(map(int,N[:i+1]))
    lst2.append(a[::-1])
lst2 = lst2[::-1]

dap = 0
for i in range(len(N)-1):
    if g(lst2[i]) == g(lst1[i]):
        dap +=1
if dap != 0:
    print("YES")
else:
    print("NO")