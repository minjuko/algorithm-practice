def solution(board, h, w):
    n = len(board)  # 1.board의 길이
    count = 0  # 2. 같은 색으로 색칠된 칸의 개수
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]  # 3.방향
    # 4.
    for i in range(4):
        # 검사할 좌표
        h_check, w_check = h + dh[i], w + dw[i]
        # 범위 설정
        if 0 <= h_check < n and 0 <= w_check < n:
            # 같은 색인지 확인
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count