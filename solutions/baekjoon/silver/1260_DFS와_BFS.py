# dfs와 bfs
from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
# 정점 수, 간선 수, 정점 번호
graph = [[0]*(n+1) for _ in range(n+1)]
visit1 = [0] * (n + 1)
visit2 = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(v):
    visit1[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if visit1[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    visit2[v] = 1
    queue.append(v)
    while(queue):
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visit2[i] = 1
dfs(v)
print()
bfs(v)



