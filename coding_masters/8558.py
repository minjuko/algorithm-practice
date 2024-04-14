# 도면 훑어보기

from collections import deque

def bfs1(x, y):
    q = deque([(x, y)])
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    visit = [[False] * 20 for _ in range(10)]
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 20 and graph[nx][ny] == '.' and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny))
    for x in range(1, 9):
        for y in range(1, 19):
            if graph[x][y] == '.' and not visit[x][y]:
                return False
    return True


def bfs2(visit):
    q = deque([(0, 0)])
    visit[0][0] = 1
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 20 and graph[nx][ny] == '#' and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
    return visit

def bfs3(x, y):
    queue = deque([(x, y)])
    num = 1
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 20 and graph[nx][ny] == '#' and not visit[nx][ny]:
                num += 1
                visit[nx][ny] = num
                queue.append((nx, ny))


n = int(input())
for _ in range(n):
    graph = [list(input().rstrip()) for _ in range(10)]
    for i in range(1, 9):
        for j in range(1, 19):
            if graph[i][j] == '.':
                i1, j1 = i, j
    result1 = bfs1(i1, j1)

    visit = [[0] * 20 for _ in range(10)]
    visit = bfs2(visit)

    for i in range(1, 9):
        for j in range(1, 19):
            if graph[i][j] == '#' and visit[i][j] == 0:
                visit[i][j] = 1
                bfs3(i, j)

    result2 = False
    for i in range(1, 9):
        for j in range(1, 19):
            if visit[i][j] >= 6:
                result2 = True
                break
        if result2:
            break

    if result1 and result2:
        print(3)
    elif result1:
        print(1)
    elif result2:
        print(2)
    else:
        print(0)
