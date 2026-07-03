# 부메랑 제작
def dfs(x, y, cnt):
    global answer

    if y == m:
        x, y = x + 1, 0
    next_x, next_y = x, y + 1
    if x == n:
        answer = max(answer, cnt)
        return

    if not visit[x][y]:
        for key in range(4):
            dx1, dy1, dx2, dy2 = dir[key]
            nx1, ny1, nx2, ny2 = x + dx1, y + dy1, x + dx2, y + dy2

            if 0 <= nx1 < n and 0 <= nx2 < n and \
                    0 <= ny1 < m and 0 <= ny2 < m and \
                    not visit[nx1][ny1] and not visit[nx2][ny2]:
                visit[x][y] = visit[nx1][ny1] = visit[nx2][ny2] = True
                dfs(next_x,
                    next_y,
                    cnt + graph[x][y] * 2 + graph[nx1][ny1] + graph[nx2][ny2])
                visit[x][y] = visit[nx1][ny1] = visit[nx2][ny2] = False

    dfs(next_x, next_y, cnt)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [-1, 0, 0, 1], 3: [0, 1, 1, 0]}
visit = [[False] * m for _ in range(n)]
answer = 0
dfs(0, 0, 0)
print(answer)
