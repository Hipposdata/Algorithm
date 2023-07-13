import sys
A, B, V = list(map(int,sys.stdin.readline().split()))

if (V-B) % (A-B) ==0:  #하루 A-B만큼 오름
    print((V-B)//(A-B))  # B만큼 떨어지므로 전날에 B만큼 덜올라도 도달하면 성공
if (V-B) % (A-B) >0:  # 총 V-B만큼 오르면 됨
    print((V-B)//(A-B)+1)
