# 쉬는 시간

n = int(input())
MOD = 998244353

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 0
dp[2] = 1

if n==0:
    print(1)
    exit()
if n==1:
    print(0)
    exit()
if n==2:
    print(1)
    exit()

for i in range(3, n+1):
    dp[i] = (i-1)* (dp[i-1] + dp[i-2]) % MOD

print(dp[n])
