# 사과 게임

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(n-i+1):
            for w in range(m-j+1):
                tmp = 0
                for x in range(k, k+i):
                    tmp += sum(graph[x][w:w+j])
                if tmp == 10:
                    answer += 1
print(answer)