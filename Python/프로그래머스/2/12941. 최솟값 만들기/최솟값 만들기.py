def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    for a,b in zip(A,B):
        answer += a*b
    return answer


# Greedy -> 최소 -> 가장큰수는 가장 작은 수랑 곱해져야함 