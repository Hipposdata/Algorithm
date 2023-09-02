lst = []

tf = True
while tf:
    try:
        a = input()
        lst.append(a)
    except EOFError: # 입력 없을시 종료
        tf = False
lst = "".join(lst)
lst = lst.replace(" ","") # 문자열 공백 제거

dic = {}
for i in lst:  # 딕셔너리형으로 문자마다 개수 세기
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

dap = []
for key, value in dic.items(): # 딕셔너리형 value max값 출력
    if max(dic.values()) == value:
        dap.append(key)

dap = sorted(dap) # 알파벳순 정렬
print("".join(dap)) # 리스트형을 문자형으로 반환

# 1. 한 줄씩 입력을 받으려면 sys.stdin.read가 아니라 sys.stdin.readline을 써야 합니다.
# 
# 2. EOFError를 사용하려면 sys.stdin.readline이 아니라 input을 써야 합니다. 만약 sys.stdin.readline을 사용하려면 다른 방법으로 EOF를 감지해야 합니다.
# 
# 3. EOFError는 예외 객체이기 때문에 if문이 아니라 try-except문을 이용해야 합니다.