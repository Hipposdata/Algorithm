def solution(s):
    # 스택 생성
    stack = []
    answer = True
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 :
                answer = False
                break
            stack.pop()

    if len(stack) >0:
        answer= False
    return answer