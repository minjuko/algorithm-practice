# 효율적인 화폐 구성

n, m = map(int, input().split()) # 동전 종류 수, 만들려는 가치 합

coins = [int(input()) for _ in range(n)] # 동전 종류

# 가치 합 m을 만들기 위한 최소 동전 개수

dp = [10001]*(m + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[m] != 10001:
    answer = dp[m]
else:
    answer = -1

print(answer)