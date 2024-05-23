# 주식 투자

n, k = map(int, input().split())
dp = [[0]*2001 for _ in range(n+1)]
dp[0][1000] = 1

for i in range(1, n+1):
    for j in range(2001):
        if 100 + j <= 2000:
            dp[i][j] += dp[i-1][j+100]
        if j - 100 >= 0:
            dp[i][j] += dp[i-1][j-100]

print(dp[n][k+1000])