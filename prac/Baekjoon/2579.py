# 계단오르기
# 한 번에 한계단 또는 두계단
# 연속된 세개 계단 밝기 금지 , 시작점 포함 x
# 마지막 반드시 밟기

n = int(input())  # 계단 수
arr = [] # 계단 입력
for _ in range(n):
    arr.append(int(input()))
dp = [0] * n

if len(arr) <= 2:    # 계단 2개 이하면 그냥 다 더해서 출력
    print(sum(arr))
else:
    dp[0] = arr[0]  # 첫 번째
    dp[1] = arr[0] + arr[1] # 두번째

    for i in range(2, n):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2]+arr[i])
        # dp[i-3] + arr[i-1] + arr[i] : i-3까지 최댓값 i-1 i 합
        # dp[i-2]+arr[i] : i-2까지 최댓값 + i
    print(dp[-1])
    # 4에 도착
    # 1) 1 3 4
    # 2) 2 4