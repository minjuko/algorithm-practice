#  아티스트 재승

k = input()
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def dfs(x, y, idx, visit):
    if len(k) <= idx:
        return visit == graph

    if graph[x][y] == k[idx] and visit[x][y] == '.':
        visit[x][y] = k[idx]
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if dfs(nx, ny, idx + 1, visit):
                    return True
        visit[x][y] = '.'
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j, 0, [['.'] * m for _ in range(n)]):
            answer += 1
print(answer)
