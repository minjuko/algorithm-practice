# 리버스 게임

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
answer = n*n

# 뒤집힌 판
board2 = [k[:] for k in board]
for i in range(n):
    for j in range(n):
        if board2[i][j] == 'B':
            board2[i][j] = 'W'
        else: board2[i][j] = 'B'

for w in range(1 << n) :
    tmp = []
    for i in range(n) :
        if w & (1 << i) :
            tmp.append(board2[i])
        else : tmp.append(board[i])

    cnt = 0
    for i in range(n) :
        col_count = 0
        for j in range(n) :
            if tmp[j][i] == 'W' :
                col_count += 1
        cnt += min(col_count, n - col_count)
    answer = min(cnt, answer)

print(answer)