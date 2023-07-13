lst =[]
count = []
for i in range(5):
    N = input()
    lst.append(N)
    count.append(len(N))

for i in range(5):
    if len(lst[i]) < max(count):
        lst[i]= lst[i]+"*"*(max(count)-len(lst[i]))

dap = []
for j in range(max(count)):
    for i in range(5):
        dap.append(lst[i][j])
        print(lst[i][j].replace("*",""), end="")