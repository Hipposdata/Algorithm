def solution(n, control):
    for i in list(control):
        if i == 'w':
            n += 1
        if i == 's':
            n -= 1
        if i == 'd':
            n+= 10
        if i == 'a':
            n-=10
    return n