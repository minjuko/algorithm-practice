# 한 번에 사과를 먹자

# 5*5
# 1 : 사과 0 : 빈 칸 -1 : 장애물
board = list(list(map(int, input().split())) for _ in range(5))
location = list(map(int, input().split())) # 현재 위치

def solution(board, location):

    # 상하좌우 이동
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 각 방향으로 이동
    for dx, dy in d:
        x, y = location[0] + dx, location[1] + dy
        if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == 1:
            return 1
    return 0

print(solution(board, location))