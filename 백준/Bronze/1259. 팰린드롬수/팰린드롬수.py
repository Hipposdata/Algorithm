tf = True
while tf:
    n = str(input())
    if n == "0":
        tf = False
    else:
        if n == n[::-1]:
            print("yes")
        elif n != n[::-1]:
            print("no")