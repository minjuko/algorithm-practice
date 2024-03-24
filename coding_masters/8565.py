# 오디세우스의 모험

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

def bfs(graph, start, end, mid):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = [start]
    while queue:
        current = queue.pop(0)
        for a, b, c in graph:
            if a == current and c >= mid and not visited[b]:
                visited[b] = True
                queue.append(b)
            if b == current and c >= mid and not visited[a]:
                visited[a] = True
                queue.append(a)
    return visited[end]

start_time = 1
end_time = 100
result = 0

while start_time <= end_time:
    mid = (start_time + end_time) // 2
    if bfs(graph, start, end, mid):
        result = mid
        start_time = mid + 1
    else:
        end_time = mid - 1

print(result)
