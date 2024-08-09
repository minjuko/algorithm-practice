# 슬라이딩 퍼즐
def move(board, x, y, nx, ny):
    new_board = [row[:] for row in board]
    new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
    return new_board

def dfs(board, n, x, y, visited, tmp):
    global answer
    if board == answer: return 0
    key = ''.join(''.join(row) for row in board)

    if key in visited:
        visited[key] = min(visited[key], tmp)
    else:
        visited[key] = tmp

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    k = -1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            new_board = move(board, x, y, nx, ny)
            new_key = ''.join(''.join(row) for row in new_board)
            if new_key not in visited or visited[new_key] > tmp:
                new_k = dfs(new_board, n, nx, ny, visited, tmp + 1)
                if new_k >= 0:
                    k = new_k + 1 if k == -1 else min(k, new_k + 1)
    return k

graph = [list(input().strip()) for _ in range(2)]
n = len(graph)
answer = [list(map(str, range(x * n + 1, x * n + 1 + n))) for x in range(n)]
answer[-1][-1] = "X"

x, y = next((i, j) for i in range(n) for j in range(n) if graph[i][j] == 'X')
print(dfs(graph, n, x, y, {}, 0))
