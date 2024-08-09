# 무향 그래프 2

n, m = map(int, input().split()) # 정점 수, 간선 수
graph = [[] for _ in range(n + 1)]  # 인접 리스트

# 간선 정보
# 오름차순 정렬
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

graph.pop(0)

# 연결된 정점 출력
for i in graph:
    if i == []:
        print("no")
    else:
        print(*i, sep=" ")