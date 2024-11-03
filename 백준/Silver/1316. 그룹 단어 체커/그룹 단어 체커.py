import sys

n = int(sys.stdin.readline())
cont = 0
for _ in range(n):
    word = sys.stdin.readline()
    tmp = word[0]
    tmp_lst = []
    for i in word:
        if tmp != i:
            tmp_lst.append(tmp)
            tmp = i
        if i in tmp_lst:
            cont+=1
            break
        # print(tmp_lst)
        # print(cont)
print(n - cont)
