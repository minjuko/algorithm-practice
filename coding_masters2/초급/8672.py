# 수하물
# k개의 가방, 하나의 가방에는 무게 제한을 넘지 않는 하나의 물건만 담기 가능
# 가져갈 수 있는 물건들의 가격의 합의 최댓값 구하기

n, k = map(int, input().split()) # 물건 수, 가방 수

# 물건 정보 (무게, 가격)
items = []
for _ in range(n):
    m, v = map(int, input().split())
    items.append((m, v))

# 가방 정보 (무게 제한)
bags =[int(input()) for _ in range(k)]

# 무게 제한 오름차순 정렬
bags.sort()

# dp[i][j]: i번째 물건까지 고려하여 j무게 제한일 때 가격의 최댓값
dp = [[0] * (bags[-1] + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, bags[-1] + 1):
        # 물건을 담을 수 없는 경우
        if items[i - 1][0] > j:
            dp[i][j] = dp[i - 1][j]
        # 물건을 담을 수 있는 경우
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][0]] + items[i - 1][1])

print(dp[n][bags[-1]]) # 최댓값 출력

