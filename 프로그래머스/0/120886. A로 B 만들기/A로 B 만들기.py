def solution(before, after):
    answer = 0
    before = sorted(list(before))
    after = sorted(list(after))
    
    if before == after:
        answer = 1
    
    
    return answer 