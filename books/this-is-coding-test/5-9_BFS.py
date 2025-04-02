# BFS 연습

from collections import deque

# bfs 메소드 정의
def bfs(graph, start, visited):
    # deque 라이브러리로 큐 구현
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결되고, 아직 방문 안한 원소들ㄹ을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드 연결 정보 2차원 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드 방문 정보
visited = [False] * len(graph)

# bfs 호출
bfs(graph, 1, visited)