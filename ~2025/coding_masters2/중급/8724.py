# 출근 시간

import heapq

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def di(idx):
    dist = [float('inf')] * (n+1)
    dist[idx] = 0
    heap = [(0, idx)]

    while heap:
        d, i = heapq.heappop(heap)
        if dist[i] < d:
            continue
        for v, w in graph[i]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (d+w, v))
    return dist

dist_s = di(1)
dist_g = di(k)

print(dist_s[k] + dist_g[n])