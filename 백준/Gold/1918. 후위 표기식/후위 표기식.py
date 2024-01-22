import sys
# 입력시 양쪽 공백 제거
exp = sys.stdin.readline().strip()
# 순위 표시된 딕셔너리 생성
dic ={'*':2, '/':2,
    '+':1,'-':1 }
# 연산자 담을 리스트(스택) 만들어줌
opt = []
# 최종답안 저장할 빈 객체
dap = ''

for i in exp:
    if i.isalpha():  # 알파벳(피연산자)인 경우 바로 dap에 추가
        dap += i
    elif i == '(':
        opt.append(i)
    elif i in dic:
        while len(opt) > 0 and  opt[-1] != '(' and dic[opt[-1]] >= dic[i]:
            dap += opt[-1]
            opt.pop()
        opt.append(i)
    elif i == ')':
        while len(opt) > 0 and opt[-1] != '(':
            dap += opt[-1]
            opt.pop()
        opt.pop()

while len(opt) > 0: # 스택에 남은 연산자 모두 dap에 추가
    dap += opt[-1]
    opt.pop()

print(dap)