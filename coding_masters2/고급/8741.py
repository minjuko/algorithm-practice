# 카드 섞기

n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

result = [0] * n
for i in range(n):
    visit = [-1] * n
    idx, cnt = i, 0

    while cnt < k:
        if visit[idx] != -1:
            tmp = cnt - visit[idx]
            for _ in range((k - cnt) % tmp):
                idx = a[idx]
            break
        visit[idx] = cnt
        idx = a[idx]
        cnt += 1
    result[idx] = i + 1

print(*result)