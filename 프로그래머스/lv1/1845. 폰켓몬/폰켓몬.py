def solution(nums):
    a = len(nums)/2
    b = len(set(nums))
    if a<=b:
        dap=a
    else:
        dap =b
    return dap