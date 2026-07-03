# 동네 한 바퀴

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([1])
while q:
    node = q.popleft()
    if node == 1 and visit[node]:
        print("YES")
        exit()
    if not visit[node]:
        visit[node] = True
        for i in graph[node]:
            q.append(i)
print("NO")




