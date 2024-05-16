# 풍수지리

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        tmp = graph[i][j]
        for k in range(i, n):
            for w in range(j, m):
                if all(graph[y][x] == tmp for y in range(i, k+1) for x in range(j, w+1)):
                    answer = max(answer, (k-i+1)*(w-j+1))

print(answer)