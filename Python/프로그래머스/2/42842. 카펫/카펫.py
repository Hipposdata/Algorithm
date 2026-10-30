# 가로 >=세로
# 세로길이 1->2->3.. 이런식으로 반복해서 적정값 찾기 
# 갈색 개수 -> 가로길이 *2 + 세로길이 *2 + 4 



def solution(brown, yellow):
    
    # 세로길이
    l = 1
    while True:
        cnt = l*2 + yellow // l * 2 + 4 
        if cnt == brown and yellow % l == 0:
            answer = [yellow // l +2,l+2]
            break
        else:
            l +=1
            
    return answer