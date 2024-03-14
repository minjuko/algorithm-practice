# 무향 그래프 1

n, m = map(int, input().split()) # 정점 수, 간선 수

graph = [[0] * n for _ in range(n)] # 인접 행렬

# 간선 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in graph:
    print(*i)
