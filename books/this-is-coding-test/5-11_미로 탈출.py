# 미로 탈출
# dfs/bfs

# nxm 직사각형 미로. 시작 위치(1,1), 출구(n, m)
# 괴물 0, 괴물 없음 1 -> 탈출하는 최소 칸의 개수 구하기

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문하는 경우만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지 최단거리
    return graph[n-1][m-1]

print(bfs(0, 0))