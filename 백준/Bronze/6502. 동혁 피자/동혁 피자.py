import sys

num = 0
tf = True
while tf:
    lst = list(map(int, sys.stdin.readline().split()))
    if len(lst) == 1:
        break
    if lst[0]*2 >= (lst[1]**2 + lst[2]**2)**(1/2):
        num += 1
        print("Pizza",num,"fits on the table.")

    elif lst[0]*2 < (lst[1]**2 + lst[2]**2)**(1/2):
        num += 1
        print("Pizza",num,"does not fit on the table.")