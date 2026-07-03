import sys
input = sys.stdin.readline

a, b = map(int, input().split())
# a개 원소에서 b개 원소를 뽑는 조합의 총 경우의 수 구하기
dp = [[0]*(b+1) for _ in range(a+1)]

for i in range(a+1):
    for j in range(min(i, b)+1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[a][b])
