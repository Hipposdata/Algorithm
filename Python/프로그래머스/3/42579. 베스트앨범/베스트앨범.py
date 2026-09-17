def solution(genres, plays):
    answer = []
    # 새로운 리스트 생성 (장르이름, 장르별 재생수, 곡별 재생수, 인덱스 )
    # 리스트 sort (lambda 이용)

    cnt = {}

    lst_gen = {}
    for i in range(len(genres)):
        lst_gen[genres[i]] = 0
        cnt[genres[i]] = 0
    
    for i in range(len(genres)):
        lst_gen[genres[i]] += plays[i]
    
    # 머지 리스트 생성 
    lst = []
    for i in range(len(genres)):
        lst.append((genres[i], lst_gen[genres[i]], plays[i], i ))
    # print(lst)        
    
    
    # 정렬
    lst.sort(key = lambda x: (-x[1], -x[2], x[3]))
    
    # 강 장르별 최대 수록곡은 2개 
    # 수록곡 수 cnt dic
    
    dap = []
    for i in lst:
        cnt[i[0]] +=1
        if cnt[i[0]] >= 3:
           continue
        else:
            dap.append(i[3])
    # print(dap)
            
    
    
    
    return dap