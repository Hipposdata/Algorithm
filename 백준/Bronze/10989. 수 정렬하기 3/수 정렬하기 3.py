import sys
n = int(sys.stdin.readline())

lst = [0] * 10001 # 총 입력 가능한 길이만큼의 리스트 생성
for i in range(n):
    lst[int(sys.stdin.readline())] += 1 # 생성한 리스트의 인덱스에 숫자 있는만큼 +1

for j in range(len(lst)): # 전체 리스트 순회하며 
    if lst[j] != 0: # 해당 인덱스가 0이 아니면 => 숫자가 들어있으면
        for _ in range(lst[j]): # 각 인덱스에는 실제 숫자 개수가 저장되어 있음 (1이면 1번등장)
            print(j)

# 즉 각 리스트의 인덱스가 실제 숫자의 값이고, 인덱스의 value는 실제 숫자의 개수가 됨 