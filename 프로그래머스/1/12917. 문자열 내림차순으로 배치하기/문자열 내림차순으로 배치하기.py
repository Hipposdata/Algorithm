def solution(s):
    up = []
    low = []
    for i in list(s):
        if i.isupper():
          up.append(i)
        else:
            low.append(i)
        
    dap = sorted(low,reverse = True) + sorted(up,reverse = True)
    
    return ''.join(dap)