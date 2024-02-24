n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 동전 k원 만드는 경우의 수 (n종류)
dp = [0 for _ in range(k+1)]
dp[0] = 1 # 0원을 만드려면 아무 것도 선택 안하는 경우

for coin in coins: # 각 동전 종류 순회
    for i in range(1, k+1):
        # coin으로 i원 만들기 -> i-coin 만든 후 coin 추가
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])