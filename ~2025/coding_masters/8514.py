# 오리 농법

n = int(input())
# n*n 밭
graph = [list(map(int, input().split())) for _ in range(n)]

# 0은 빈 땅, 1은 작물, 2는 잡초
# 오리는 가로.세로줄의 잡초, 작물 모두 먹음
# 적절하게 작물을 보존하면서 최대한 많은 잡초 없애기

answer = 0 # 잡초만 있는 땅 개수

for i in range(n):
    if 1 not in graph[i]:
        graph[i] = [0]*n

graph = list(zip(*graph))

for i in range(n):
    if 1 not in graph[i]:
        graph[i] = [0]*n

for i in range(n):
    answer += graph[i].count(2)

print(answer)