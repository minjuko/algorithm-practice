# 두더지 게임

# 두더지는 0에서만 올라오기 가능 1은 구멍
# 올라올 수 있는 칸의 개수 구하기

# 8*8 판
graph = [input().rstrip() for _ in range(8)]

answer = 0

# 8x8 크기의 빈 배열 생성
board = [[0] * 8 for _ in range(8)]

# 각 행을 반복하면서 패턴에 맞게 0과 1을 번갈아가며 채움
for i in range(8):
    for j in range(8):
        if (i + j) % 2:
            board[i][j] = 1

for i in range(8):
    for j in range(8):
        if board[i][j] == 0 and graph[i][j] == 'F':
            answer += 1
print(answer)