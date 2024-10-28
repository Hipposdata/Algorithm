import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
cont = 0
i = 0
while True:
    # print(i)
    if i >= len(s) - len(t)+1:
        break
    if s[i:i + len(t)] == t:
        cont += 1
        i += len(t) -1
    i +=1
print(cont)