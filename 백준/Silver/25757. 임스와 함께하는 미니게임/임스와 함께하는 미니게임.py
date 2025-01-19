import sys

n, game = sys.stdin.readline().split()

n = int(n)
lst = []
set = set()
for _  in range(n):
    name = sys.stdin.readline().strip()
    set.add(name)
# list로 할시 시간초과 / set자료형 이용하기
if game == 'Y':
    print(len(set) // 1)
elif game == 'F':
    print(len(set) // 2)
else:
    print(len(set) // 3)



