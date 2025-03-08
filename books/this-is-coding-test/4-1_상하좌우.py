# [구현] 상하좌우

# L, R, U, D 상하좌우 이동
# 최종 도착지점 좌표 구하기

n = int(input()) # n*n 정사각형 공간
plans = input().split() # 이동 계획(L,R,U,D)
x, y = 1, 1 # 시작 좌표

# 이동 방향을 딕셔너리로 정의 (dx, dy를 하나로 묶음)
movements = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

for plan in plans:
    dx, dy = movements[plan]
    nx, ny = x + dx, y + dy

    # 범위를 벗어나면 무시
    if not (1 <= nx <= n and 1 <= ny <= n):
        continue

    x, y = nx, ny

print(x, y)
