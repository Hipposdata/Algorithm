def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def n2t(num):
        
        num = int(num[:2]) *60 + int(num[3:])
        return num
            
    time = n2t(pos)
    
        
    if n2t(op_start) <= time <= n2t(op_end):
        time = n2t(op_end)
        
    for com in commands:
        if com == 'prev':
            if time < 10:
                time = 0
            else:
                time -= 10
        elif com == 'next':
            time += 10
    
        if time > n2t(video_len):
            time = n2t(video_len)
        if n2t(op_start) <= time <= n2t(op_end):
            time = n2t(op_end)
    
    
    
    hour = str(time//60) 
    mt = str(time%60) 
    
    if int(hour) <10:
        hour = "0" + hour
    if int(mt) < 10:
        mt = "0" + mt
    answer = hour + ":" + mt

    return answer