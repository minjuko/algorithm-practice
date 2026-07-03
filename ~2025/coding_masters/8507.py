# 주사위의 합

n = int(input())

# 주사위 2개를 굴려 합이 n이 되는 경우의 수
for i in range(1, 7):
    for j in range(1, 7):
        if i+j == n:
            print(i, j)