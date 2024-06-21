def solution(order):
    answer = 0
    for i in list(str(order)):

        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer