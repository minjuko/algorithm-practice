# 약육강식

# 일렬로 상어 -> 뒤에 있는 상어가 앞에 있는 상어보다 크다면 삼킬 수 있음
# 연속적으로 먹히는 관계를 가진 상어의 최대 마리 수 구하기

n = int(input()) # 상어 수
sharks = list(map(int, input().split())) # 상어 크기

dp = [1]*n # dp[i] = i번째 상어가 마지막 상어일 때 최대 마리 수

for i in range(n):
    for j in range(i):
        # i번째 상어가 j번째 상어를 먹을 수 있다면
        if sharks[i] > sharks[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))