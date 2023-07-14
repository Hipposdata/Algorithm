def find_yaksu(n):
    yaksu = []
    for i in range(1, n + 1):
        if n % i == 0:
            yaksu.append(i)
    return yaksu

yaksu = []
tf = True
while tf:
    n = int(input())
    if n ==-1:
        tf = False
    else:
        find_yaksu(n)  # 함수 정의 -> 약수 확인하는
        yaksu_sum = sum(find_yaksu(n)[:-1])

        if yaksu_sum == n:  # 완전수 확인
            yaksu = list(map(str, find_yaksu(n)[:-1]))
            print(n, "=", " + ".join(yaksu))
        else:
            print(f"{n} is NOT perfect.")