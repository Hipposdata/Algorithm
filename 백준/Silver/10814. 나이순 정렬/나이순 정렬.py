import sys
n = int(sys.stdin.readline())

data = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    data.append([int(age), name])

# 버블 정렬 -> 시간초과 발생
# sort함수 이용 / lambda이용 -> 정렬 순서 정해줌
data.sort(key=lambda x: x[0])
for q in range(n):
    data[q] = list(map(str, data[q]))
    print(' '.join(data[q]))
