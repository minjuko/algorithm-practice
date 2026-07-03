# 8688 그룹ID

from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
def solve(graph, n):
    def dfs(node, visited, group):
        visited[node] = True
        group.add(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, group)

    max_id = None
    max_size = 0
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            group = set()
            dfs(i, visited, group)
            if len(group) > max_size:
                max_size = len(group)
                max_id = min(group)

    return max_id

answer = solve(graph, n)
print(answer)
