# XOR

n = int(input())
nums = list(map(int, input().split()))

dp = {0: 1}
for num in nums:
    tmp_dp = dp.copy()
    for k in dp:
        tmp = k ^ num
        if tmp in tmp_dp:
            tmp_dp[tmp] += dp[k]
        else:
            tmp_dp[tmp] = dp[k]
    dp = tmp_dp

print(dp[0] - 1)