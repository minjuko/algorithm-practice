# 파스칼 피라미드
import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for k in range(1, n):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i + j <= k:
                tmp[i][j] = dp[i][j]
                if 0 <= i - 1:
                    tmp[i][j] += dp[i - 1][j]
                if 0 <= j - 1:
                    tmp[i][j] += dp[i][j - 1]
    dp = tmp

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0:
            print(dp[i][j], end=' ')
    print()
