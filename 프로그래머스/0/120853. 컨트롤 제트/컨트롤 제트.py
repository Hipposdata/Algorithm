def solution(s):
    answer = 0
    lst = s.split(' ')
    dap = []
    print(lst)
    for i in lst:
        if i != 'Z':
            dap.append(i)
        elif i == 'Z':
            dap.pop()
    dap = list(map(int,dap))
    answer = sum(dap) 

    return answer