# 추가되거나 제거된 문자열만 반영함
import sys
s, p = map(int,sys.stdin.readline().split())
lst = list(sys.stdin.readline().strip())
acgt = list(map(int,sys.stdin.readline().split()))

start = 0
end = p
cont = 0
chek = [lst[start:end].count('A'), lst[start:end].count('C'),
       lst[start:end].count('G'), lst[start:end].count('T')]

while end <= s :
    # 각 문자가 acgt에서 요구하는 최소 개수 이상일 경우
    if chek[0] >= acgt[0] and chek[1] >= acgt[1] and chek[2] >= acgt[2] and chek[3] >= acgt[3]:
        cont += 1

    if lst[start] == 'A':
        chek[0] -=1
    if lst[start] == 'C':
        chek[1] -=1
    if lst[start] == 'G':
        chek[2] -= 1
    if lst[start] == 'T':
        chek[3] -= 1

    if end == s:
        break

    if lst[end] == 'A':
        chek[0] +=1
    if lst[end] == 'C':
        chek[1] +=1
    if lst[end] == 'G':
        chek[2] +=1
    if lst[end] == 'T':
        chek[3] +=1

    start += 1
    end += 1
print(cont)