import sys
# 스택구조에 넣으면서 에러기 나거나 최종구조에 여분이 남아 있으면 no출력

st =[] # 빈 스택구조 생성
def stck(lst):
    for i in range(len(lst)):
        if lst[i] =="(":
            st.append(0)
        else:
            if len(st) != 0:
                st.pop()
            else:
                return "NO"
        if i == len(lst)-1:
            if len(st) == 0:
                return "YES"
            else:
                return "NO"

T = int(sys.stdin.readline())
for i in range(T):
    lst = sys.stdin.readline().rstrip()    # 입력된 리스트구조
    print(stck(lst))
    st= []
