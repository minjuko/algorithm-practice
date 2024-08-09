# 그림 감상

graph = [input() for _ in range(4)]

for i in range(3):
    for j in range(3):
        cnt = 0 # X 수
        if graph[i][j] == 'X':
            cnt += 1
        if graph[i][j + 1] == 'X':
            cnt += 1
        if graph[i + 1][j] == 'X':
            cnt += 1
        if graph[i + 1][j + 1] == 'X':
            cnt += 1
        if cnt >= 3:
            print("yes")
            exit(0)
print("no")