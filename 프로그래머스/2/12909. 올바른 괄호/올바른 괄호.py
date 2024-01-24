def solution(s):
    answer = True
    dap = 0
    for i in s:
        if i == '(':
            dap +=1
        else:
            dap -=1
        if dap <0 :
            answer = False
    if dap != 0:
        answer = False
    return answer