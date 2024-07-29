
money = int(input())

left_money = 1000 - money
cont = 0
while left_money >= 500:
    left_money -= 500
    cont += 1
while left_money >= 100:
    left_money -= 100
    cont += 1
while left_money >= 50:
    left_money -= 50
    cont += 1
while left_money >= 10:
    left_money -= 10
    cont += 1
while left_money >= 5:
    left_money -= 5
    cont += 1
while left_money >= 1:
    left_money -= 1
    cont += 1
print(cont)