import sys

a = sys.stdin.readline().split()
# 월별 누적일수
m_d = { 'January':0, 'February':31, 'March':59,
      'April':90, 'May':120, 'June':151, 'July':181, 'August':212, 'September':243,
      'October':273, 'November':304, 'December':334}
m = m_d[a[0]]
d= int(a[1][:2])
y = int(a[2])
h =int(a[3][0:2])
minute = int(a[3][-2:])

if y % 4 ==0 :
    if (y % 100 !=0 and y%400 !=0) or (y % 100 ==0 and y%400 ==0) :
        if a[0] != 'January' and  a[0] != 'February':
            print((((m + d) * 24 * 60 + h * 60 + minute) / (366 * 24 * 60)) * 100)
        else:
            print((((m + d-1) * 24 * 60 + h * 60 + minute) / (366 * 24 * 60)) * 100)
    else:
        print((((m + d - 1) * 24 * 60 + h * 60 + minute) / (365 * 24 * 60)) * 100)
else:
    print((((m + d - 1) * 24 * 60 + h * 60 + minute) / (365 * 24 * 60)) * 100)

