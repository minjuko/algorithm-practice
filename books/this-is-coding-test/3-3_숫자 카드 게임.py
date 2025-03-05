# 숫자 카드 게임
# 각 행의 가장 작은 값들 중 가장 큰 값을 찾는다.

# min() 함수 활용

n, m = map(int, input().split()) # 행, 열

result = 0 #
for i in range(n):
    data = list(map(int, input().split())) # 각 행 입력 받기
    min_value = min(data) # 해당 행의 가장 작은 값
    result = max(result, min_value) # 가장 작은 값 중 가장 큰 값

print(result)
