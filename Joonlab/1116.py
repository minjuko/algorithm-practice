# 세 번 이내에 사과를 먹자

# 5*5 보드판
# 1:사과 0:빈칸 -1:장애물
# 상하좌우 3번 이하 이동으로 사과 2개 이상 먹을 수 있는지 확인

board = list(list(map(int, input().split())) for _ in range(5)) # 5*5 보드판
location = list(map(int, input().split())) # 초기 위치
def check(board, location, x1, x2, x3):
    cnt = 0  # 먹을 수 있는 사과 수

    # 사과 2개를 먹을 수 없는 상황 판단
    # 1번, 2번 이동 위치가 보드판을 벗어나는 경우
    if not (0 <= x1[0] < 5 and 0 <= x1[1] < 5) or not (0 <= x2[0] < 5 and 0 <= x2[1] < 5):
        return 0
    # 1번, 2번 이동 위치에 장애물이 있는 경우
    if board[x1[0]][x1[1]] == -1 or board[x2[0]][x2[1]] == -1:
        return 0
    # 2번 이동 위치가 출발 위치와 같은 경우 (기존 위치는 장애물 칸이 됨)
    if x2 == location:
        return 0

    # 1번, 2번 사과 수 갱신
    cnt = board[x1[0]][x1[1]] + board[x2[0]][x2[1]]
    # 3번 사과 수 갱신
    if 0 <= x3[0] < 5 and 0 <= x3[1] < 5 and board[x3[0]][x3[1]] == 1 and x1 != x3:
        cnt += 1
    return cnt


def solution(board, location):
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 방향

    # 상하좌우 3번 이동 시 판단
    for i in range(4):
        for j in range(4):
            for k in range(4):
                # 1번, 2번, 3번 이동 위치 계산
                x1 = [location[0] + d[i][0], location[1] + d[i][1]]
                x2 = [x1[0] + d[j][0], x1[1] + d[j][1]]
                x3 = [x2[0] + d[k][0], x2[1] + d[k][1]]

                if check(board, location, x1, x2, x3) >= 2: # 사과 2개 이상 먹으면 1
                    return 1
    return 0

print(solution(board, location))