# 교도소

def check(v, e, edges):
    def dfs(node, tmp):
        relations[node] = tmp
        for neighbor in graph[node]:
            if neighbor not in relations:
                if not dfs(neighbor, 1 - tmp):
                    return False
            elif relations[neighbor] == tmp:
                return False
        return True

    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    relations = {}
    for i in range(1, v + 1):
        if i not in relations:
            if not dfs(i, 0):
                return 0
    return 1

v, e = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(e)]
print(check(v, e, graph))
