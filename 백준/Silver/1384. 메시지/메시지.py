import sys
count = 0
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    count += 1
    if count >1 :
        print()
        print(f'Group {count}')
    else:
        print(f'Group {count}')

    lst = []
    for _ in range(n):
        tmp = list(sys.stdin.readline().strip().split())
        lst.append(tmp)
    memo = 0
    for i in range(len(lst)):
        for j in range(1,len(lst[i])):
            if lst[i][j] == 'P':
                pass
            elif lst[i][j] == 'N':
                memo = 1
                if i+1 - j < 0:
                    print(f'{lst[i+1 + len(lst) - 1 - j][0]} was nasty about {lst[i][0]}' )
                else:
                    print(f'{lst[i - j][0]} was nasty about {lst[i][0]}' )

    if memo == 0:
        print('Nobody was nasty')