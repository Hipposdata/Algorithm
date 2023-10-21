import sys

num = int(sys.stdin.readline())

for i in range(num):
    quiz = list(sys.stdin.readline()[:-1])
    hap = 0
    chonghap = []
    for j in quiz:
        if j == 'X':
            hap = 0
        elif j == 'O':
            hap +=1
            chonghap.append(hap)
    print(sum(chonghap))