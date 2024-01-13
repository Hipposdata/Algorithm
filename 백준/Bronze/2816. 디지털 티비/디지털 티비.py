import sys
n = int(sys.stdin.readline())

lst = []
for i in range(n):
    lst.append(sys.stdin.readline()[:-1])

def arrowdown(cursor):
    cursor += 1
    print(1, end ='')
    return cursor

def channelup(cursor):
    if cursor >0:
        lst[cursor], lst[cursor-1] = lst[cursor-1],  lst[cursor]
        cursor -= 1
        print(4,end ='')
    return cursor

cursor = 0
while True:
    if lst[cursor] != 'KBS1':
            cursor = arrowdown(cursor)
    elif lst[cursor] == 'KBS1':
            cursor = channelup(cursor)
    if lst[0] == 'KBS1':
        break

while True:
    if lst[cursor] != 'KBS2':
        cursor = arrowdown(cursor)
    elif lst[cursor] == 'KBS2':
        cursor = channelup(cursor)
    if lst[1] == 'KBS2':
        break
