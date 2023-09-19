import sys

lst1 = map(int,sys.stdin.readline().split())
lst2 = map(int,sys.stdin.readline().split())

hap1 = sum(lst1)
hap2 = sum(lst2)

if hap1 > hap2:
    print(hap1)
elif hap1 < hap2:
    print(hap2)
elif hap1 == hap2:
    print(hap1)