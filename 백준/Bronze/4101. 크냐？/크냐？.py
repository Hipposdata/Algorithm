import sys

tf = True
while tf:
     f, s = map(int,sys.stdin.readline().split())
     if f==0 and s == 0:
         tf = False
     else:
         if f > s:
             print("Yes")
         else:
             print("No")