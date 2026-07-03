# 약육강식

# 일렬로 상어 -> 뒤에 있는 상어가 앞에 있는 상어보다 크다면 삼킬 수 있음
# 연속적으로 먹히는 관계를 가진 상어의 최대 마리 수 구하기

n = int(input())
sharks = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if sharks[i] > sharks[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))