import sys
n = int(sys.stdin.readline())

lst = [str(i) for i in range(111,999+1) if len(set(str(i))) == 3 and '0' not in str(i)]
dap = []

for _ in range(n):
    num, s,b = sys.stdin.readline().strip().split()
    tmp = set()
    for i in lst:
        s_c = 0
        b_c = 0
        for j in range(0,3):
            if i[j] == num[j]: # 각 자리 값 동일한지 비교
                s_c +=1
            elif i[j] in num: # 자리수는 다른데 있는경우
                b_c +=1
        if s == str(s_c) and b == str(b_c):
            tmp.add(i)
    dap.append(tmp)

rs =set(dap[0])
for i in dap[1:]:
    rs = rs&i

print(len(rs))