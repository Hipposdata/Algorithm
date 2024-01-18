def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if r == i % q:
            answer += code[i]
    return answer