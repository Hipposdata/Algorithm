
import sys
mn, mx = map(int, sys.stdin.readline().split())
# cont = 0
minus = []

lst = [True] * (mx - mn +1)
for i in range(2,int(mx**0.5)+1):
    sq= i*i
    gop = mn // sq
    # start = mn // sq
    while sq*gop <= mx: # 겹치는 수 제거되지 않게됨
        if mn <= sq*gop <=mx:
            minus.append(sq*gop)
        gop += 1
# for k in lst:
#     if k:
#         cont +=1
print((mx - mn +1) - len(set(minus)) )