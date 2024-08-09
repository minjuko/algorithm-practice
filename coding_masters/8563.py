#  영화제

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
visit = [-1 for _ in range(n)]
answer = 0

def dfs(x):
    for i in graph[x]:
        if flag[i]:
            continue
        flag[i] = 1
        if visit[i] == -1 or dfs(visit[i]):
            visit[i] = x
            return True
    return False

for i in range(n-1):
    for j in range(i+1, n):
        if points[i][0] >= points[j][0] and points[i][1] >= points[j][1] and points[i][2] >= points[j][2]:
            graph[i].append(j)
        elif points[i][0] <= points[j][0] and points[i][1] <= points[j][1] and points[i][2] <= points[j][2]:
            graph[j].append(i)

for i in range(n):
    flag = [0 for _ in range(n)]
    if dfs(i):
        answer += 1
    flag = [0 for _ in range(n)]
    if dfs(i):
        answer += 1
print(n - answer)
