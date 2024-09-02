N,k = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))

lst.sort(reverse = True)


dap = 0
for i in lst:
    if k == 0:
        break
    if k >= i:
        dap += k // i
        k %= i

print(dap)