# 음식 배달

def dfs(idx, visit, start):
    global answer

    if visit.count(True) == k:
        answer = min(answer, start + house[idx][2])
        return
    for i in range(n):
        if not visit[i]:
            next = start + abs(house[idx][0] - house[i][0]) + abs(house[idx][1] - house[i][1])
            if next < answer:
                visit[i] = True
                dfs(i, visit, next)
                visit[i] = False

n, k = map(int, input().split())
house = []
for _ in range(n):
    x, y = map(int, input().split())
    house.append((x-1, y-1, x-1+y-1))

answer = float('inf')

for i in range(n):
    visit = [False] * n
    visit[i] = True
    dfs(i, visit, house[i][2])

print(answer)
