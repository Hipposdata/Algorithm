def solution(s):
    lst = s.split(' ')
    rst = []
    
    for i in lst:
        if i == '':  # 1. 연속 공백(빈 문자열) 방어: 비어있으면 그대로 리스트에 넣고 다음으로!
            rst.append(i)
            
        elif i[0].isdigit():  # 2. 첫 글자가 숫자일 때
            word = i[0] + i[1:].lower()  # 첫 글자는 그대로 두고, 나머지만 소문자로!
            rst.append(word)
            
        else:  # 3. 첫 글자가 알파벳일 때
            word = i[0].upper() + i[1:].lower()  # 오타(.) 수정!
            rst.append(word)
         
    answer = ' '.join(rst)
    return answer