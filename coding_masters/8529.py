# 떡 하나 주면 안 잡아먹지

def bfs(graph):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = graph[0][0]

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 다이나믹 프로그래밍 진행
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    dp[nx][ny] = min(dp[nx][ny], dp[i][j] + graph[nx][ny])

    return dp[n - 1][n - 1]

# 입력 받기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(bfs(graph))
