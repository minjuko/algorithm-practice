# 사과 빨리 먹기

board = list(list(map(int, input().split())) for _ in range(5)) # 5*5 보드판
location = list(map(int, input().split())) # 초기 위치

# 사과 3개를 먹기 위한 최소 이동 횟수

def solution(board, location, apple):
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 방향

    if apple == 0:
        return 0 # 사과 3개를 먹은 경우 종료
    cnt = -1 # 최소 이동 횟수 (초기값 -1)

    for dx, dy in d:
        x, y = location[0] + dx, location[1] + dy
        if 0 <= x < 5 and 0 <= y < 5 and board[x][y] != -1:
            prev = board[location[0]][location[1]] # 이전 위치
            board[location[0]][location[1]] = -1 # 현재 위치를 장애물로 변경

            cur_cnt = solution(board, [x, y], apple - board[x][y]) # 현재 위치에서 1회 이동
            if cur_cnt != -1:
                cur_cnt += 1
            if cur_cnt != -1:
                if cnt == -1 or cur_cnt < cnt:
                    cnt = cur_cnt
            board[location[0]][location[1]] = prev
    return cnt

print(solution(board, location, 3))
