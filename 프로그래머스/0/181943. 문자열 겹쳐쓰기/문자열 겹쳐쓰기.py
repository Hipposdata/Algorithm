def solution(my_string, overwrite_string, s):
    start = my_string[:s]
    rep = my_string[s:s+len(overwrite_string)].replace(my_string[s:s+len(overwrite_string)],overwrite_string,1)
    end = my_string[s+len(overwrite_string):]

    answer = start + rep + end
    return  answer


