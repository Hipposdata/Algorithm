str = input()
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


dap = []
for i in range(len(str)):
    for j in range(len(small)):
        if str[i] == small[j]:
            dap+= big[j]
    for k in range(len(big)):
        if str[i] == big[k]:
            dap+= small[k]
    
        
print(''.join(dap))