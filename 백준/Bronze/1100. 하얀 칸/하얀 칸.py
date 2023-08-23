import sys
hap = 0
for j in range(1,9):
    iprek = sys.stdin.readline()
    if j%2 == 0: # 짝수행
        for i in range(8):
            if (i + 1) % 2 == 0:
                if iprek[i] == 'F':
                    hap += 1
    else: # 홀수행
        for i in range(8):
            if (i + 1) % 2 != 0:
                if iprek[i] == 'F':
                    hap += 1
print(hap)