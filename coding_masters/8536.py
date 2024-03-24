# 콘웨이의 생명 게임

import sys
input = sys.stdin.readline
n = int(input())
graph = [list(input().strip()) for _ in range(5)]

for _ in range(n):
    new_board = [['0'] * 5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            cnt = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and graph[nr][nc] == '1':
                        cnt += 1
            if graph[r][c] == '1':
                new_board[r][c] = '1' if cnt == 2 or cnt == 3 else '0'
            else:
                new_board[r][c] = '1' if cnt == 3 else '0'
    graph = new_board

for row in graph:
    print(''.join(row))
