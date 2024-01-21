# 제일 큰수값을 저장할 빈틀 만들어서 number 값을 하나씩 비교하면서 넣음 
# 빈틀에는 비교하는 number 값보다 크거나 같은 값이 들어가도록 하기
def solution(number, k):
    # 빈 틀 만들기
    lst = []
    # enumerate 함수 이용 -> 인덱스 번호와 값 불러옴
    for i, num in enumerate(number):  
    # 빈틀에 값이 있고(없으면 마지막 값 비교못함), 빈틀 마지막 값이 number값보다 작고, 남은 제거할 횟수(k)가 존재할때 반복
        while len(lst) > 0 and lst[-1] < num and k >0:
            lst.pop()
            k -=1
    # 남은 제거할 횟수(k) 없을때 멈춤
        if k == 0:
            lst += list(number[i:])   
            break
        lst.append(num)
   # 제거할 횟수(k)가 남았지만 이미 큰수값이 다 들어가 있는 경우     
    if k > 0:
        lst = lst[:-k]
    answer = ''.join(lst)
    return answer