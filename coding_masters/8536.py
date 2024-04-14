# 콘웨이의 생명 게임

import sys
input = sys.stdin.readline
n = int(input())
graph = [list(input().strip()) for _ in range(5)]

for _ in range(n):
    new_board = [['0'] * 5 for _ in range(5)]
    for x in range(5):
        for y in range(5):
            cnt = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and graph[nx][ny] == '1':
                        cnt += 1
            if graph[x][y] == '1':
                new_board[x][y] = '1' if cnt == 2 or cnt == 3 else '0'
            else:
                new_board[x][y] = '1' if cnt == 3 else '0'
    graph = new_board

for row in graph:
    print(''.join(row))
