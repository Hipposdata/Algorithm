# 큐 활용
from collections import deque


def solution(cards1, cards2, goal):
    answer = ''
    goal_q = deque(goal)
    cards1_q = deque(cards1)
    cards2_q = deque(cards2)
    
    while True:
                    
        if len(goal_q) ==0:
            answer = 'Yes'
            break
    
        if cards1_q and cards1_q[0] == goal_q[0]:
            goal_q.popleft()
            cards1_q.popleft()
        elif cards2_q and cards2_q[0] == goal_q[0]:
            goal_q.popleft()
            cards2_q.popleft()
        else: 
            answer = 'No'

            break
        
        
    return answer