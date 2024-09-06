# 양쪽 포인터를 사용
import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

cont = 0

for i in lst:
    start_idx = 0
    end_idx = len(lst) - 2
    lst.remove(i)
    while start_idx < end_idx:
        # print(lst)
        # print(f"num: {i}")
        # print(f"start: {start_idx}")
        # print(f"end: {end_idx}")
        # print(f"cont: {cont}")
        # print("---------------")
        if lst[start_idx] + lst[end_idx] == i:
            cont += 1
            break
        elif lst[start_idx] + lst[end_idx] < i:
            start_idx += 1
        else: # lst[start_idx] + lst[end_idx] > i
            end_idx -= 1
    lst.append(i)
    lst.sort()

print(cont)