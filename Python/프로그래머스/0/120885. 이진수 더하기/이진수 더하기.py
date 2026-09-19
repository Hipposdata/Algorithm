def solution(bin1, bin2):
    answer = ''
    hap = int(bin1,2) + int(bin2,2)
    
    
    answer = bin(hap)[2:]
    
    return answer