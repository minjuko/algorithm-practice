# 부업

for _ in range(int(input())):
    n, k = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    flag = False
    for i in range(51):
        for j in range(51):
            if a1*i + b1*j == n and a2*i + b2*j == k:
                flag = True
                break
    if flag:
        print('YES')
    else:
        print('NO')