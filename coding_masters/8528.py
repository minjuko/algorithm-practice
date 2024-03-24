# 바닥 공사 3

# 가로 n, 세로 2 직사각형 바닥
# 1x2, 2x1 덮개를 이용하여 바닥을 채우는 경우의 수 구하기

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[n])