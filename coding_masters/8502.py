# N을 보는 시각

n = int(input())

# 00:00:00 ~ 23:59:59까지 n이 등장하는 횟수 구하기

answer = 0

# 시분초 24*60*60 돌면서 n 포함 시 업데이트
for h in range(24):
    for m in range(60):
        for s in range(60):
            if str(n) in str(h) + str(m) + str(s):
                answer += 1
print(answer)