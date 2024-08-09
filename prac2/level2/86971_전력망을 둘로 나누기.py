from collections import deque


def solution(n, wires):
    answer = 100000
    graph = [[] for _ in range(n + 1)]

    # 양쪽 모두 추가
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)


    # 주어진 전선 중 하나를 끝어 두 전력망으로 나누는 경우
    for a, b in wires:
        visited = [False for _ in range(n + 1)]
        q = deque()
        q.append(a) #
        cnt = 1 # 현재 전력망 크기 갱신
        visited[a] = True # a 방문
        visited[b] = True # b 방문

        while q:
            # 큐에서 노드를 꺼내 해당 노드와 연결된 모든 노드에 대해
            # 방문하지 않은 경우 전력망 크기 갱신
            x = q.popleft()
            for i in graph[x]:
                if not visited[i]:
                    cnt += 1
                    visited[i] = True
                    q.append(i)

        min_data = min(cnt, n - cnt) # 전력망 크기 중 가장 작은 값
        max_data = n - min_data # 전력망 크기 중 가장 큰 값
        # 크기 차이 갱신
        if answer > max_data - min_data:
            answer = max_data - min_data
    return answer
