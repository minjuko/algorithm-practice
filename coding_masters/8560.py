# 탈출사건

from collections import deque

n, m = map(int, input().split())
zoo = [list(map(int, input().split())) for _ in range(n)]
leo = [(i, j) for i in range(n) for j in range(m) if zoo[i][j] == 2]
answer = 0
def dfs(wall, idx):
    global answer
    if wall == 3:
        tmp = [[zoo[i][j] for j in range(m)] for i in range(n)]
        q = deque(leo)
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0),  (0, -1), (-1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append((nx, ny))
        safe = sum(row.count(0) for row in tmp)
        answer = max(answer, safe)
        return

    for i in range(idx, n * m):
        x, y = i // m, i % m
        if zoo[x][y] == 0:
            zoo[x][y] = 1
            dfs(wall + 1, i + 1)
            zoo[x][y] = 0

dfs(0, 0)
print(answer)
