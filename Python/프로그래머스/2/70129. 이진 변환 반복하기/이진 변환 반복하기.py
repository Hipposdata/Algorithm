def solution(s):
    answer = [0,0]
    no = 0
    cnt = 0
    
    while True:

        
        if s == '1':
            break
        hap = 0            
        
        for i in s:
            if i == '1':
                hap +=1
            else:
                no +=1
        cnt +=1
        s = bin(hap)[2:]
    
    
    answer[0] = cnt
    answer[1] = no
    
    return answer