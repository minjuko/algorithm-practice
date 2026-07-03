# 묵찌빠봇

n, m = map(int, input().split())

bot1 = list(map(int, input().split()))
bot2 = list(map(int, input().split()))

def solve(x, y):
    if x==y:
        return 0
    elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        return 1
    else:
        return 2


flag = 0
i = 0
j = 0
cnt = 0
max_cnt = n * m + 1

while cnt < max_cnt:
    x = bot1[i]
    y = bot2[j]

    check = solve(x, y)

    if flag != 0 and check == 0:
        print(flag)
        break
    else:
        flag = check
        cnt += 1

    i = (i + 1) % n
    j = (j + 1) % m
else:
    print(0)
