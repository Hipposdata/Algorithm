iprek = str(input())
a = "c="
b = "c-"
c = "dz="
d = "d-"
e = "lj"
f = "nj"
g = "s="
h = "z="
hap = [a,b,c,d,e,f,g,h]

for i in range(len(hap)):
    if hap[i] in iprek:
        iprek = iprek.replace(hap[i],".")


print(len(iprek))
