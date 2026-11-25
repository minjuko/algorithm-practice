# 유기농 배추
# 1은 배추 땅 0은 배추 X
# 상하좌우 인접한 배추는 흰지렁이 하나 필요
# 최소 흰지렁이 수 구하기
from collections import deque

def bfs(graph, a, b):
    d = [[1,0], [-1,0], [0,1], [0,-1]] # 상하좌우
    q = deque()
    q.append((a,b)) # 시작점
    graph[a][b] = 0 # 방문 처리 # 방문 처리
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            # 범위 내 + 배추밭이면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문 처리
                q.append((nx, ny))
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 위치 수
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split()) # 배추 위치
        graph[y][x] = 1 # 배추 위치 1로 표시
    answer = 0
    # 모든 칸에 대해 탐색
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                answer += 1
    print(answer)

