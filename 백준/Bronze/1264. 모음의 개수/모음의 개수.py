import sys

vowel = ['a','e','i','o','u','A','E','I','O','U']
while True:
    cnt = 0
    sentence = list(sys.stdin.readline()[:-1])
    if len(sentence) == 1 and '#' in sentence:
        break
    else:
        for i in sentence:
            if i in vowel:
                cnt +=1
        print(cnt)