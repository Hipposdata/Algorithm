def solution(keymap, targets):
    answer = []
    for t in targets:
        
        
        # 타겟 내부 요소하나씩접근
        cnt = 0
        for ta in t:
                        
            # 최솟값
            mn = 9999999999999999
            
            for n_k, k in enumerate(keymap):
                # 키맵 요소 하나씩 접근
                for n_k_yoso, k_yoso in enumerate(k):
                    if k_yoso == ta and mn > n_k_yoso:                       
                        
                        mn = n_k_yoso +1
            
            if mn == 9999999999999999:
                cnt = -1
                break
            
            cnt += mn

        answer.append(cnt)
            # 타겟 요소에 해당하는 값 없는 경우        
            # if 

    
    return answer