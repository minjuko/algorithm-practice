# 숫자 맞추기

# 시작 숫자에 +1, -1, *2 연산을 반복하여 목표숫자에 도달하는 최소 횟수 구하기

n, k = map(int, input().split()) # 목표 숫자, 시작 숫자

if n <= k:
    answer = k - n
    print(answer)
    exit()
dp = [float('inf')] * (n + 1)
dp[k] = 0

for i in range(k, n+1):
    if dp[i] == float('inf'):
        continue
    if i+1 <= n:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if i*2 <= n:
        dp[i*2] = min(dp[i*2], dp[i]+1)
    if i-1 >= 0:
        dp[i-1] = min(dp[i-1], dp[i]+1)
print(dp[n])