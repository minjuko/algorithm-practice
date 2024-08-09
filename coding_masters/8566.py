# 교도소

v, e = map(int, input().split()) # 죄수 수, 친한 죄수 쌍 수
graph = [list(map(int, input().split())) for _ in range(e)] # 친한 죄수 쌍

def check(v, edges):
    def dfs(node, tmp):

        # 현재 죄수의 구역 설정
        # 현재 죄수와 연결된 죄수 탐색
        relations[node] = tmp

        for neighbor in graph[node]:
            # 연결된 죄수가 아직 구역 설정이 안되었다면
            if neighbor not in relations:
                # 현재 죄수와 다른 구역으로 설정하고 dfs
                if not dfs(neighbor, 1 - tmp):
                    return False
            # 이미 구역이 같게 설정되어있다면 종료
            elif relations[neighbor] == tmp:
                return False
        return True

    graph = {}
    # 그래프 설정 (양방향)
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    relations = {} # 구역

    # 모든 죄수에 대해 dfs 탐색
    for i in range(1, v + 1):
        if i not in relations:
            if not dfs(i, 0):
                return 0 # 구역 설정 불가능 시 0
    return 1

print(check(v, graph))
