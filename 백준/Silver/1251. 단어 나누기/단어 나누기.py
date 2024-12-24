import sys

word = sys.stdin.readline().strip()

lst = []
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        rv = word[0:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        lst.append(rv)


lst.sort()
print(lst[0])