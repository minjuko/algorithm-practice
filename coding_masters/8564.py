# 막사 정찰

# 28사단 헌병은 밤마다 1번 막사와 2번 막사 사이를 정찰합니다.
#
# 날이 추워 가만히 있으면 손발이 꽁꽁 얼기 때문에 헌병은 두 막사를 최대한 많이 왕복하려고 합니다.
#
#
#
# 막사를 방문할 때마다 정찰일지에 서명을 하는데,
#
# 1번, 2번 막사를 제외한 나머지 막사엔 서명이 1개 이상 있으면 안됩니다.
#
# 단, 한번의 왕복 과정에서 방문했던 막사를 또 방문하게 되면 서명을 생략합니다.
#
#
#
# 막사들은 서로 양방향 길로 이어져 있습니다.
#
# 그리고 1번 막사와 2번 막사를 왕복할 때는 반드시 한 개 이상의 다른 막사를 들러야 합니다.
#
# 1번 막사와 2번 막사를 왕복할 수 있는 최대 횟수를 출력합니다.

# 첫째 줄에 막사의 수 N (3 ≤ N ≤ 100)과 막사들 사이의 길의 개수 P (1 ≤ P ≤ 1,000)가 주어집니다.
#
# 다음 P개의 줄에는 각 길이 연결하는 서로 다른 두 막사의 번호가 주어집니다.
#
# 1번 막사와 2번 막사를 직접 연결하는 길은 없습니다.
#
# 출력값 설명
#
# 첫째 줄에 1번 막사와 2번 막사를 왕복할 수 있는 최대 횟수를 출력합니다

# 입력1
# 3 2
# 1 3
# 2 3

# 출력1
# 1

# 입력2
# 5 7
# 1 3
# 1 4
# 1 5
# 2 3
# 2 4
# 2 5
# 3 4

# 출력2
# 3

def dfs(graph, visited, start, end, count):
    visited[start] = True

    if start == end and count >= 2:
        return 1

    result = 0
    for neighbor in graph[start]:
        if not visited[neighbor]:
            result += dfs(graph, visited, neighbor, end, count + 1)

    visited[start] = False
    return result


def max_patrol(graph, start, end):
    visited = [False] * len(graph)
    return dfs(graph, visited, start, end, 0)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

print(max_patrol(graph, 0, 1))
