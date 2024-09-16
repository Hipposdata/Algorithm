# 쁠러스 값 다 더하고 마지막에 다 뺌


import sys
# lst = list(sys.stdin.readline().strip())
lst = list(map(str, sys.stdin.readline().strip().split('-')))

first = 0
hap = 0
for i in range(0,len(lst)):
    if i == 0:
        if '+' in lst[i]:
            first += sum(list(map(int, lst[i].split("+"))))
        else:
            first += int(lst[i])

    else:
        if '+' in lst[i]:
            hap += sum(list(map(int,lst[i].split("+"))))
        else:
            hap += int(lst[i])

print(first - hap)