N = int(input())

lst = []
lst = '*'*N
lst = ' '.join(lst)
for i in range(1,N+1):
    if i%2==0:
        print('',lst)
    else:
        print(lst)