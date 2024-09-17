import sys
n = int(sys.stdin.readline())


# lst = [False] *2 + [True] * (1000000 - 1)
# for i in range(2, int(1000000 ** (1 / 2)) + 1):
#     if lst[i] == True:
#         for j in range(i * i, 1000000 + 1, i):
#             lst[j] = False

def prime(num):
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

while True:
    if n == 1:
        print(2)
        break
    if prime(n):
        if list(str(n)) == list((str(n))[::-1]):
            print(n)
            break
    n +=1