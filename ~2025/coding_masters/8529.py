# 떡 하나 주면 안 잡아먹지

import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[float('inf')] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x, y = 0, 0
q = [(graph[x][y], x, y)]
result[x][y] = graph[x][y]

while q:
    dist, x, y = heapq.heappop(q)
    if result[x][y] < dist:
        continue
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            cnt = dist + graph[nx][ny]
            if cnt < result[nx][ny]:
                result[nx][ny] = cnt
                heapq.heappush(q, (cnt, nx, ny))
print(result[n - 1][n - 1])
