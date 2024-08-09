# 8674 달고나

from collections import deque

n, m = map(int, input().split()) # 세로, 가로
graph = [input() for _ in range(n)] # 구멍 정보
visit = [[0] * m for _ in range(n)]
answer = 0

def bfs(x, y):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 상하좌우
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '0' and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and not visit[i][j]:
            answer += 1
            bfs(i, j)
print(answer)
