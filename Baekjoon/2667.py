# 단지번호 붙이기
# 1은 집 0은 집 아님
# 연결(상하좌우)된 집의 모임 단지에 번호 붙이기
# 단지 수와 각 단지별 집의 수 오름차순으로 출력

from collections import deque
n = int(input())
graph = [list(map(int, input())) for _ in range(n)] # n*n
answer = [] # 각 단지별 집의 수 저장할 배열

def bfs(a, b):
    q = deque()
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우
    q.append((a, b))  # 시작점
    count = 1 # 단지 내 집의 수

    while q:
        x, y = q.popleft()  # 큐에서 좌표 꺼내서
        graph[x][y] = 0 # 방문 처리
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1: # 범위 내에 있고 집이면
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

# 좌표 하나씩 돌기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)
