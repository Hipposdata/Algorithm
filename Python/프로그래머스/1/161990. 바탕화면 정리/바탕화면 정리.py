# 각 행렬 min, max값 반환 
# 행최소, ,열최소, 

def solution(wallpaper):
    r_lst = []
    c_lst = []
    for r in range(0,len(wallpaper)):
        for c in range(0,len(wallpaper[0])):
           if wallpaper[r][c] == '#':
            r_lst.append(r)
            c_lst.append(c)
    print(r_lst, c_lst)
    answer = [min(r_lst), min(c_lst), max(r_lst)+1, max(c_lst)+1] 
    return answer