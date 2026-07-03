# 마법의 지팡이

n = int(input())
cnt = 0 # 사용 횟수

while n != 1:
    if n % 2 == 0:
        n //= 2
        cnt += 1
    elif n % 3 == 0:
        n //= 3
        n *= 2
        cnt += 1
    elif n % 5 == 0:
        n //= 5
        n *= 4
        cnt += 1
    else:
        cnt = -1
        break

if cnt == -1:
    print(-1)
else:
    print(cnt)