def solution(bandage, health, attacks):
    answer = 0
    
    # 기술은 계속 써지는중 
    
    skill = 0 # 스킬 연속적 사용 판단 
    time = 0  
    atck = 0 # 공격 순서 
    h_max = health
    while True:
        time +=1 
        print(health)
        
        # 공격받은경우
        if time == attacks[atck][0]:
            skill = 0
            health -= attacks[atck][1]
            atck +=1
        
        # 공격받지 않은 경우
        else:
            skill +=1
            health += bandage[1]

            if health >= h_max:
                health = h_max

                
        # 연속적 스킬사용
        if skill == bandage[0]:
            health += bandage[2] # 추가회복량 
            skill = 0
            if health >= h_max:
                health = h_max
            
            
        # 멈춤 요건 
        if health <=0 or time == attacks[-1][0]:
            break    

    answer = health
    if answer <=0:
        answer = -1
    
    return answer