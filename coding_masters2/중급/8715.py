# 메타버스 토끼

from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = [[False] * m for _ in range(n)]
q = deque([(0, 0, 0)])

while q:
    x, y, cnt = q.popleft()
    if x == n - 1 and y == m - 1:
        print(cnt)
        exit()
    if visit[x][y]:
        continue

    visit[x][y] = True

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        nx2, ny2 = x+2*dx, y+2*dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
            if 0 <= nx2 < n and 0 <= ny2 < m and graph[nx2][ny2] == '.':
                q.append((nx2, ny2, cnt+1))
            else:
                q.append((nx, ny, cnt+1))
print(-1)
