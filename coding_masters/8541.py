# 슬라이딩 퍼즐

import sys
import copy

def dfs(board, N, x, y, visited, tmp):
    global answer
    if board == answer: return 0
    key = id(board)

    if key in visited:
        visited[key] = tmp if visited[key] > tmp else visited[key]
    else:
        visited[key] = tmp

    k = -1
    if x > 0:
        new = copy.deepcopy(board)
        new[x][y], new[x - 1][y] = new[x - 1][y], new[x][y]
        key = id(new)
        if not key in visited or visited[key] > tmp:
            new_k = dfs(new, N, x - 1, y, visited, tmp + 1)
            if new_k >= 0:
                k = new_k + 1 if new_k + 1 < k or k < 0 else k

    if x < N - 1:
        new = copy.deepcopy(board)
        new[x][y], new[x + 1][y] = new[x + 1][y], new[x][y]
        key = id(new)
        if not key in visited or visited[key] > tmp:
            new_k = dfs(new, N, x + 1, y, visited, tmp + 1)
            if new_k >= 0:
                k = new_k + 1 if new_k + 1 < k or k < 0 else k
    if y > 0:
        new = copy.deepcopy(board)
        new[x][y], new[x][y - 1] = new[x][y - 1], new[x][y]
        key = id(new)
        if not key in visited or visited[key] > tmp:
            new_k = dfs(new, N, x, y - 1, visited, tmp + 1)
            if new_k >= 0:
                k = new_k + 1 if new_k + 1 < k or k < 0 else k

    if y < N - 1:
        new = copy.deepcopy(board)
        new[x][y], new[x][y + 1] = new[x][y + 1], new[x][y]
        key = id(new)
        if not key in visited or visited[key] > tmp:
            new_k = dfs(new, N, x, y + 1, visited, tmp + 1)
            if new_k >= 0:
                k = new_k + 1 if new_k + 1 < k or k < 0 else k
    return k

graph = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))
n = len(graph)
answer = list(map(lambda x: list(map(str, range(x * n + 1, x * n + 1 + n))), range(n)))
answer[-1][-1] = "X"
id = lambda x: ''.join(list(map(lambda k: ''.join(k), x)))

x, y = -1, -1
for i in range(n):
    if 'X' in graph[i]:
        x, y = i, graph[i].index('X')
        break

print(dfs(graph, n, x, y, {}, 0))