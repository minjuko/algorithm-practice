def max_boomerang_strength(N, M, material):
    max_strength = 0
    for i in range(N):
        for j in range(M):
            # ㄱ 모양의 부메랑을 만들 수 있는 경우를 탐색
            if j + 2 < M:
                boomerang_strength = material[i][j] * 2 + material[i][j + 1] + material[i][j + 2]
                max_strength = max(max_strength, boomerang_strength)
            if i + 2 < N:
                boomerang_strength = material[i][j] * 2 + material[i + 1][j] + material[i + 2][j]
                max_strength = max(max_strength, boomerang_strength)
            if i + 1 < N and j + 1 < M:
                boomerang_strength = material[i][j] * 2 + material[i + 1][j] + material[i + 1][j + 1]
                max_strength = max(max_strength, boomerang_strength)
                boomerang_strength = material[i][j] * 2 + material[i][j + 1] + material[i + 1][j + 1]
                max_strength = max(max_strength, boomerang_strength)
    return max_strength

N, M = map(int, input().split())
material = [list(map(int, input().split())) for _ in range(N)]

print(max_boomerang_strength(N, M, material))
