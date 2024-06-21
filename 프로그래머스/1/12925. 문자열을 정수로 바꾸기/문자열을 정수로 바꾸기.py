def solution(s):
    if s[0] == '+':
        num = int(s[1:])
    if s[0] == '-':
        num = int(s[1:]) * -1
    else:
        num = int(s)

    return num