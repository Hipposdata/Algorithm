import sys

s = sys.stdin.readline().strip()

ch1 = 0
ch0 = 0
if s[0] == '1':
    ch1 += 1
else:
    ch0 += 1
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        if s[i] == '1':
            ch1 +=1
        else:
            ch0 +=1

print(min(ch0,ch1))
