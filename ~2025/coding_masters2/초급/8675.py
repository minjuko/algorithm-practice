# 병원

import heapq

n = int(input()) # 정류장 수
m = int(input()) # 버스 경로 수

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u - 1].append((v - 1, t))
    graph[v - 1].append((u - 1, t))

s, e = map(int, input().split())

def solve(start, end, graph):
    n = len(graph)
    dist_arr = [float('inf')] * n
    dist_arr[start] = 0
    q = [(0, start)]

    while q:
        dist, node =heapq.heappop(q)
        if node == end:
            return dist_arr[end]
        if dist > dist_arr[node]:
            continue
        for a, b in graph[node]:
            tmp = dist + b
            if tmp < dist_arr[a]:
                dist_arr[a] = tmp
                heapq.heappush(q, (tmp, a))
    return dist_arr[end]

print(solve(s-1, e-1, graph))

