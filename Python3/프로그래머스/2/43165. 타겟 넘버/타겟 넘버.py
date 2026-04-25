# dfs  모든 경우의수 
# cnt +=1
# 모든 숫자를 이용해서 덧뺄셈으로 만들어야함

def solution(numbers, target):
    
    giho = [-1, 1]
    stck = [] 
    stck.append((0,0))
    # 타겟 만족횟수
    cnt = 0
    # 사용한 숫자 수 
    
    while stck:
        cur_sum, idx = stck.pop()
        
        if idx == len(numbers):
            if cur_sum == target:
                cnt+=1
            continue
            
        cur_num = numbers[idx]
        
        # 가능한 모든 조합 
        for i in giho:
            nn = cur_sum + (i * cur_num)
            stck.append((nn, idx +1))
    return cnt


