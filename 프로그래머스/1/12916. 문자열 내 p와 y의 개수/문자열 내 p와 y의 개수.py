def solution(s):
    answer = True
    pcont = 0
    ycont = 0
    for i in list(s):
        if i == 'P' or i == 'p':
            pcont +=1
        if i == 'Y' or i == 'y':
            ycont +=1
    if pcont == ycont:
        answer = True
    else:
        answer = False
    return answer