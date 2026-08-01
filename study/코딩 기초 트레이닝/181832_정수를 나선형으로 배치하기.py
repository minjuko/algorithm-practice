def solution(n):
    # 1. n × n 배열 생성
    board = [[0] * n for _ in range(n)]

    # 2. 이동 방향: 오른쪽 → 아래 → 왼쪽 → 위
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    # 3. 배열 범위 내부인지 확인
    def is_inside(row, col):
        return 0 <= row < n and 0 <= col < n

    row, col = 0, 0
    direction_idx = 0

    # 4. 1부터 n²까지 순서대로 배치
    for number in range(1, n * n + 1):
        board[row][col] = number

        dr, dc = directions[direction_idx]
        next_row = row + dr
        next_col = col + dc

        # 5. 범위를 벗어나거나 이미 방문한 칸이면 방향 전환
        if (
            not is_inside(next_row, next_col)
            or board[next_row][next_col] != 0
        ):
            direction_idx = (direction_idx + 1) % 4

            dr, dc = directions[direction_idx]
            next_row = row + dr
            next_col = col + dc

        # 6. 다음 위치로 이동
        row, col = next_row, next_col

    return board