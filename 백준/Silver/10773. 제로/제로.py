import sys
k = int(sys.stdin.readline())

st = []
for _ in range(k):
    a  = int(sys.stdin.readline())
    if a !=0:
        st.append(a)
    else:
        st.pop()
print(sum(st))
