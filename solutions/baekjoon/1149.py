# RGB 거리

n = int(input()) # 집의 수
graph = [list(map(int, input().split())) for _ in range(n)] # 각 집을 칠하는 비용

# 빨, 초, 파 중 하나 -> 모든 집을 칠하는 비용의 최솟값
# 1번 색 != 2번 색
# n번 색 != n-1번 색
# i번 색 != i-1번 색, i+1번 색

for i in range(1, n):
    graph[i][0] = min(graph[i-1][1], graph[i-1][2]) + graph[i][0] # i번 집을 빨간색으로 칠할 때 최솟값
    graph[i][1] = min(graph[i-1][0], graph[i-1][2]) + graph[i][1] # i번 집을 초록색으로 칠할 때 최솟값
    graph[i][2] = min(graph[i-1][0], graph[i-1][1]) + graph[i][2] # i번 집을 파란색으로 칠할 때 최솟값
print(min(graph[n-1]))
