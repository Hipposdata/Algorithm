import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

start_idx = 0
end_idx = n-1
cont = 0

while start_idx < end_idx:
    # print(f"start: {start_idx}")
    # print(f"end: {end_idx}")
    # print(f"cont: {cont}")
    # print("---------------")
    if lst[end_idx] + lst[start_idx] == m:
        cont +=1
        start_idx += 1
        end_idx -= 1
    elif lst[end_idx] + lst[start_idx] < m:
        start_idx += 1
    else: # lst[end_idx] + lst[start_idx] > m:
        end_idx -= 1
print(cont)