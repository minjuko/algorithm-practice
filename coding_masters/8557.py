# 한 줄 지우기 오목

graph = [list(input()) for _ in range(10)]
answer = []
def win(graph):
    dir = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 'W':
                for dx, dy in dir:
                    cnt = 1
                    for k in range(1, 5):
                        nx, ny = i + dx * k, j + dy * k
                        if 0 <= nx < 10 and 0 <= ny < 10 and graph[nx][ny] == 'W':
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        return True
    return False

def cnt_move(graph, idx):
    cnt = 0
    global answer
    for i in range(10):
        for j in range(10):
            if graph[i][j] == '.':
                graph[i][j] = 'W'
                if win(graph):
                    if(i, j, idx) not in answer:
                        answer.append((i, j, idx))
                    cnt += 1
                graph[i][j] = '.'
    return cnt

graph = [list(row) for row in zip(*graph)]
total_cnt = 0

for i in range(10):
    tmp = graph[i].copy()
    graph[i] = ['.']*10
    total_cnt += cnt_move(graph, "가로"+str(i))
    graph[i] = tmp

for i in range(10):
    tmp2 = [graph[j][i] for j in range(10)]
    for j in range(10):
        graph[j][i] = '.'
    total_cnt += cnt_move(graph, "세로"+str(i))

    for j in range(10):
        graph[j][i] = tmp2[j]

print(total_cnt)
