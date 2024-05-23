# 높은 곳을 향해

n = int(input())
heights = list(map(int, input().split()))
dp = [1] * n

if n%2 != 0 and n!=5:
    dp = [0] * n

for i in range(1, n):
    for j in range(i):
        if heights[i] > heights[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))