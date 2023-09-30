import sys

buger = []
beverage = []

for i in range(3):
    price = int(sys.stdin.readline())
    buger.append(price)

for j in range(2):
    price2 = int(sys.stdin.readline())
    beverage.append(price2)


print(min(buger)+ min(beverage)-50)