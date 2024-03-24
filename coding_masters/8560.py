# 탈출 사건

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 0: 빈칸, 1: 울타리, 2: 재규어

# 상하좌우 이동
# 3개의 여분 울타리를 설치해 재규어가 도달할 수 없는 칸 수 최대화
# 여분 울타리는 빈 칸에만 설치 가능 (설치 시 울타리 칸)
# 재규어는 상하좌우 인접한 칸 이동
# 재규어가 도달할 수 벗는 빈 칸 수 출력

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = graph[0][0]

    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    dp[nx][ny] = min(dp[nx][ny], dp[i][j] + graph[nx][ny])

    return dp[n - 1][n - 1]

def solution(n, m, graph):
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                answer = max(answer, bfs(graph))
                graph[i][j] = 0

    return answer

print(solution(n, m, graph))
