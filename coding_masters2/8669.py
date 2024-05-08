# 깊이 우선 탐색

n, m = map(int, input().split()) # 정점 수, 간선 수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) # 방문 여부

# 양방향 연결
# 탐색한 인접한 정점 중 정점번호가 작은 정점부터
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

# dfs 탐색
def dfs(v):
    visited[v] = True
    print(v, end=" ") # 현재 정점 출력

    # 현재 정점과 연결된 인접 정점에 대해 탐색
    for i in graph[v]:
        # 방문하지 않은 정점에 대해 dfs
        if not visited[i]:
            dfs(i)

dfs(1) # 1번 정점부터 시작

