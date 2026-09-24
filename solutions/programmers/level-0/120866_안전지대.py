def solution(board):
    bomb = set()  # 지뢰의 위험 지역이 겹칠 때 한 번만 저장
    n = len(board)

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(n):
        for col in range(n):
            # 지뢰 위치에서 주변 좌표 탐색
            if board[row][col] == 1:
                for dx, dy in directions:
                    x = row + dx
                    y = col + dy
                    # 범위 확인
                    if 0 <= x < n and 0 <= y < n:
                        bomb.add((x, y))
    # 전체 칸 (n*n) - 위험한 칸
    return n * n - len(bomb)