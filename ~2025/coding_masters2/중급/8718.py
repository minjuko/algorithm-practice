# 격자판 칠하기

n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
cnt = 0

def dfs(x, y):
    global cnt
    for i in range(1, 4):
        if (x == 0 or graph[x-1][y] != i) and (y == 0 or graph[x][y-1] != i):
            graph[x][y] = i
            nx, ny = (x + (y + 1) // m), (y + 1) % m
            if nx == n:
                cnt += 1
            else:
                dfs(nx, ny)
            graph[x][y] = 0

dfs(0, 0)
print(cnt)
