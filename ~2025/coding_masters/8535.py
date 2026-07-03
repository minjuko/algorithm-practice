# 같은 그래프

from itertools import combinations

n1, m1 = map(int, input().split()) # 1번 그래프 정점 수, 간선 수
graph1, graph2 = [], []

# 간선 정보 정렬하여 저장
for _ in range(m1):
    u, v = map(int, input().split())
    graph1.append((min(u, v), max(u, v)))

n2, m2 = map(int, input().split()) # 2번 그래프 정점 수, 간선 수
for _ in range(m2):
    u, v = map(int, input().split())
    graph2.append((min(u, v), max(u, v)))

def check(u, v, graph):
    # 정점 번호를 바꾸어 새 그래프를 생성
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
        new_graph.append((min(i, j), max(i, j))) # 정렬
    return new_graph

# 가능한 조합 모두 고려하여 두 그래프가 동일한지 판별

result = [(graph1, [])]
while result:
    tmp_graph, remain = result.pop() # 비교 기준 그래프, 방문 X 노드 리스트

   # 집합 비교
   # 동일하면 두 그래프가 동일한 것으로 판별
    if set(tmp_graph) == set(graph2):
        print('YES')
        exit()

    # 사용 X 노드 조합
    nodes = [i for i in range(1, n1 + 1) if i not in remain]
    # 노드를 조합하여 새 그래프 생성
    for u, v in list(combinations(nodes, 2)):
        new_graph = check(u, v, tmp_graph)
        result.append((new_graph, remain + [u])) # 새 그래프, 방문 노드 추가

print('NO') # 모든 경우 탐색 후 찾지 못한 경우 동일하지 않은 것으로 판단
