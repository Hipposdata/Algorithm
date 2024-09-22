
import sys

lst = list(sys.stdin.readline().strip())

stack = []
dap = 0
tmp = 1

# 괄호열의 유효성 여부를 판단하는 변수
valid = True

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
        tmp *= 2  # '('를 만나면 tmp에 2를 곱함

    elif lst[i] == '[':
        stack.append(lst[i])
        tmp *= 3  # '['를 만나면 tmp에 3을 곱함

    elif lst[i] == ')':
        # 잘못된 괄호열인 경우 (스택이 비어있거나 짝이 맞지 않는 경우)
        if not stack or stack[-1] != '(':
            valid = False
            break
        # 직전 괄호가 '('인 경우 tmp 값을 dap에 더함
        if lst[i-1] == '(':
            dap += tmp
        # 스택에서 '('를 제거하고 tmp를 2로 나눔
        stack.pop()
        tmp //= 2

    elif lst[i] == ']':
        # 잘못된 괄호열인 경우 (스택이 비어있거나 짝이 맞지 않는 경우)
        if not stack or stack[-1] != '[':
            valid = False
            break
        # 직전 괄호가 '['인 경우 tmp 값을 dap에 더함 -> 중복된 닫히는 괄호 )) ]] 나왔을때 직전괄호가 열리는 거여야만 저장됨
        if lst[i-1] == '[':
            dap += tmp
        # 스택에서 '['를 제거하고 tmp를 3으로 나눔
        stack.pop()
        tmp //= 3

    else:
        valid = False
        break

# 스택이 비어있지 않으면 올바르지 않은 괄호열
if stack:
    valid = False

# 결과 출력
if valid:
    print(dap)
else:
    print(0)