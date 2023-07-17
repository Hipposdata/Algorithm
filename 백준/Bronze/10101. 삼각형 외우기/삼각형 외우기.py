
lst = []
for i in range(3):
    n = int(input())
    lst.append(n)

if lst[0] + lst[1] + lst[2] ==180:
    if lst[0] == lst[1] == lst[2]==60:
        print("Equilateral")
    if lst[0]==lst[1] !=lst[2] or lst[1] ==lst[2] !=lst[0] or lst[0] ==lst[2] !=lst[1]:
        print("Isosceles")
    if lst[0] != lst[1] and lst[1] != lst[2] and lst[0] != lst[2]:
        print("Scalene")
else:
    print("Error")