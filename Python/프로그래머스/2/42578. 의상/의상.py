# 각 종류별로 몇개씩 있는지 파악 -> dic
# 하나씩 + 각 종류 곱

def solution(clothes):
    answer = 0
    dic = {}
    for i in clothes:
        a,b = i[0], i[1]
        dic[b] = []
        
    for i in clothes:
        a,b = i[0], i[1]
        dic[b].append(a)
        
    cnt = 1
    for a,b in dic.items():
        cnt *= (len(b)+1)
        print(cnt)
    
    answer = cnt-1
    

    return answer