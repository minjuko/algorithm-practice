from itertools import combinations

n1, m1 = map(int, input().split())
graph1, graph2 = [], []

for _ in range(m1):
    u, v = map(int, input().split())
    graph1.append((min(u, v), max(u, v)))

n2, m2 = map(int, input().split())
for _ in range(m2):
    u, v = map(int, input().split())
    graph2.append((min(u, v), max(u, v)))

def check(u, v, graph):
    new_graph = []
    for i, j in graph:
        if i == u:
            i = v
        elif i == v:
            i = u
        if j == u:
            j = v
        elif j == v:
            j = u
        new_graph.append((min(i, j), max(i, j)))
    return new_graph

result = [(graph1, [])]
while result:
    tmp_graph, remain = result.pop()

   # 집합 비교
    if set(tmp_graph) == set(graph2):
        print('YES')
        exit()

    # 사용 X 노드 조합
    nodes = [i for i in range(1, n1 + 1) if i not in remain]
    for u, v in list(combinations(nodes, 2)):
        new_graph = check(u, v, tmp_graph)
        result.append((new_graph, remain + [u]))

print('NO')
