# 인간 사각형

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def check(x1, y1, x2, y2):
    return graph[x1][y1] == graph[x2][y1] == graph[x1][y2] == graph[x2][y2]

for i in range(n):
    for j in range(m):
        for k in range(1, min(n-i, m-j)):
            if check(i, j, i+k, j+k):
                tmp = (k+1) * (k+1)
                answer = max(answer, tmp)

print(answer)