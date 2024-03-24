# 탈출 사건

# 빈동은 동물원의 안전 책임자입니다.
#
# 동물원은 N행 M열의 격자, 총 N × M 칸으로 나눌 수 있습니다.
#
#
#
# 어느 날 재규어들이 우리에서 탈출했습니다.
#
# 이 재규어들은 매우 공격적이라 당장 포획할 수 없습니다.
#
# 빈동은 입장객들에게 대피하라고 알린 뒤, 날뛰는 재규어를 막을 방법을 찾아냈습니다.
#
#
#
# 동물원은 빈 칸, 재규어가 있는 칸, 울타리가 있는 칸으로 구분할 수 있습니다.
#
# 재규어들은 상하좌우 중 한 방향으로 인접한 빈 칸으로 이동할 수 있으며, 동물원 밖으로 나가지 못합니다.
#
#
#
# 빈동의 목표는 3개의 여분 울타리를  모두 설치해, 재규어가 도달할 수 없는 칸의 수를 최대화 하는 것입니다.
#
# 여분 울타리는 빈 칸에만 설치할 수 있고, 설치하면 그 칸은 울타리가 있는 칸이 됩니다.
#
#
#
# 빈동이 목표를 달성했을 때,
#
# 재규어가 도달할 수 없는 빈 칸의 수를 출력하는 프로그램을 작성하세요.

# 입력1
# 4 4
# 0 1 0 0
# 1 0 2 0
# 0 1 0 0
# 0 0 1 1

# 출력1
# 6
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    global graph
    queue = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.pop(0)
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

def dfs(cnt):
    global graph
    if cnt == 3:
        bfs()
        result = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    result += 1
        return result
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                result = max(result, dfs(cnt + 1))
                graph[i][j] = 0
    return result

print(dfs(0))
