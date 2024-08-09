# 머니 게임

n, m = map(int, input().split())

while n!=0 and m!=0:
    if 2*n <= m:
        m %= 2*n
    elif 2*m <= n:
        n %= 2*m
    else:
        break
print(n, m)
