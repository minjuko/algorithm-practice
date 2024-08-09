# 그림판

from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

red, blue = 0, 0

def bfs(red, blue):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((red, blue))

    cnt1, cnt2 = 0, 0
    while q:
        red, blue = q.popleft()

        if visit[red][blue]:
            continue
        else:
            if graph[red][blue] == 'A':
                cnt1 += 1
            elif graph[red][blue] == 'B':
                cnt2 += 1
            visit[red][blue] = 1

            for dx, dy in d:
                nx, ny = red + dx, blue + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] != 'X' and not visit[nx][ny]:
                        q.append((nx, ny))
    if cnt1 > cnt2:
        return cnt1, 0
    else:
        return 0, cnt2

for i in range(n):
    for j in range(m):
        if graph[i][j] != 'X' and not visit[i][j]:
            tmp1, tmp2 = bfs(i, j)
            red += tmp1
            blue += tmp2
print(red, blue)