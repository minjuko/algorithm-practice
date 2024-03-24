# # 인간 사각형
def max_square_area(N, M, grid):
    max_area = 0
    for i in range(N):
        for j in range(M):
            for k in range(N):
                for l in range(M):
                    if grid[i][j] == grid[k][l]:
                        side = abs(k - i) + 1
                        if l + side - 1 < M and grid[i][j] == grid[i + side - 1][l] and grid[i][j] == grid[k + side - 1][l]:
                            max_area = max(max_area, side * side)
    return max_area

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(max_square_area(N, M, grid))
