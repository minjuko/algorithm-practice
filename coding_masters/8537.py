# 콩벌레

graph = []
for i in range(10):
    state = list(map(int, input()))
    if 2 in state:
        start = [i, state.index(2)]
    graph.append(state)

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dir = 0

visit = 1
cnt = 0

while True:
    if cnt == 2:
        print("no")
        break

    nx, ny = start[0] + d[dir][0], start[1] + d[dir][1]
    if not (0 <= nx < 10 and 0 <= ny < 10):
        print("yes")
        break
    else:
        if graph[nx][ny] == 1:
            if visit:
                dir = (dir + 1) % 4
            else:
                dir = (dir + 3) % 4
            visit = 1 - visit
            cnt += 1
        else:
            start = [nx, ny]
            cnt = 0

