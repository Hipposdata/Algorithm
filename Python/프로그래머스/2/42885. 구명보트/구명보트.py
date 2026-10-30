from collections import deque

# 제일큰값, 작은값 빼기 
# 합 비교 
def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    q = deque(people)
    print(q)
    cnt = 0
    while len(q) >0:
        if len(q) == 1:
            cnt+=1
            break
        
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
            cnt+=1
        else:
            q.popleft()
            cnt+=1
    
    return cnt