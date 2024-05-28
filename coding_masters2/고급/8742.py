# 심야 버스

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def floyd():
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = graph[i][j]
        for k in range(n):
            for w in range(n):
                for v in range(n):
                    if result[w][k] and result[k][v]:
                        result[w][v] = 1
    return result

result = floyd()
for i in range(n):
    print(*result[i])