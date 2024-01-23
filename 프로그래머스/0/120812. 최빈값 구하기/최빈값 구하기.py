def solution(array):
    answer = 0
    lst = {}
    for i in array:
        lst[i] = array.count(i)
    ls = sorted(lst.items(),key = lambda x: x[1],reverse = True)
    print(ls)
    if len(ls) >1:
        if ls[0][1] == ls[1][1]:
            answer = -1
        else:
            answer = ls[0][0]
    else:
        answer = ls[0][0]
    return answer