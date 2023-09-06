import sys

tf = True
while True:
    name, age, weight = sys.stdin.readline().split()
    age, weight = int(age), int(weight)
    if name == "#" and age== 0 and weight== 0:
        break
    else:
        if (age >17) or (weight >=80):
            print(name, 'Senior')
        else:
            print(name, 'Junior')
