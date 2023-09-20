import sys

lst1 = list(sys.stdin.readline()[:-1])
lst2 = list(sys.stdin.readline()[:-1])


if len(lst1) < len(lst2):
    print('no')
else:
    print('go')