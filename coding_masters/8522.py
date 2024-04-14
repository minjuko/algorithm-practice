# 먹보 수민이

n = int(input())
info = []
for _ in range(n):
    a, b = map(int, input().split()) # 거리, 포만감
    info.append((a, b))
d, p = map(int, input().split())
visit = [0]*d

for idx, [a, b] in enumerate(info):
    if d <= a+b:
        b = max(0, d-a)
    info[idx] = [a, b]
info.sort(key=lambda x: (-x[1], x[0]))

answer = 0
for a, b in info:
    if visit.count(0) <= p:
        break
    for i in range(b+1):
        if d > a+i:
            visit[a+i] = 1
    answer += 1

if visit.count(0) > p:
    print(-1)
else:
    print(answer)

