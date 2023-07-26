N = int(input())
from collections import deque
lst = deque()

for i in range(1,N+1):
    lst.append(i)
if len(lst) == 1:
    print(lst[0])
while len(lst) >0:
    lst.popleft()
    if len(lst) == 1:
        print(lst[0])
    if len(lst) > 1:
        lst.append(lst[0])
        lst.popleft()