# 동전 줍기

# 삼각형 형태의 산의 정상에서 내려가면서 최대 동전 줍기
# 바로 아래로 내려가거나, 한 칸 오른쪽으로 내려가기

n = int(input()) # 산의 높이
graph = [list(map(int, input().split())) for _ in range(n)] # 동전 개수

dp = [[0]*n for _ in range(n)] # dp[i][j] = (i, j)까지 도달했을 때 최대 동전 개수
dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + graph[i][0]
    dp[i][i] = dp[i - 1][i - 1] + graph[i][i]

    for j in range(1, i):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + graph[i][j]

answer = max(dp[n - 1])
print(answer)
