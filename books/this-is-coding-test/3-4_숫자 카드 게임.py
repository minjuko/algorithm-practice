# 숫자 카드 게임
# 각 행의 가장 작은 값들 중 가장 큰 값을 찾는다.

# 2중 반복문 구조 풀이

n, m = map(int, input().split()) # 행, 열

result = 0 #
for i in range(n):
    data = list(map(int, input().split())) # 각 행 입력 받기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)