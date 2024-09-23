import sys
m = int(sys.stdin.readline())

s = set()
for _ in range(m):
    iprek = list(sys.stdin.readline().strip().split())
    if len(iprek) >1:
        iprek[1] = int(iprek[1])

    if iprek[0] == 'add':
        if iprek[1] not in s:
            s.add(iprek[1])
    elif iprek[0] == 'remove':
        if iprek[1]  in s:
            s.remove(iprek[1])
    elif iprek[0] == 'check':
        if iprek[1] in s:
            print(1)
        else:
            print(0)
    elif iprek[0] == 'toggle':
        if iprek[1] in s:
            s.remove(iprek[1])
        else:
            s.add(iprek[1])
    elif iprek[0] == 'all':
        s = set(range(1,21))
    elif iprek[0] == 'empty':
        s = set()
