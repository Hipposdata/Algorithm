def solution(number, k):
    answer = ''
    lst = []
    # enumerate 함수 이용 -> 인덱스 번호와 값 불러옴
    for i, num in enumerate(number):  
        while len(lst) > 0 and lst[-1] < num and k >0:
            lst.pop()
            k -=1
        if k == 0:
            lst += list(number[i:])   # 남은 제거할 수 없을때 멈춤
            break
        lst.append(num)
    if k > 0:
        lst = lst[:-k]
    answer = ''.join(lst)
    return answer