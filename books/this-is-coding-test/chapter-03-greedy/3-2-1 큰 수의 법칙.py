# 큰 수의 법칙
# 1. 주어진 수를 m번 더해 가장 큰 수를 만든다.
# 2. 특정 인덱스의 수는 연속 k번 초과하여 더할 수 없다.

n, m, k = map(int, input().split()) # n: 배열의 크기
data = list(map(int, input().split())) # 배열
result = 0 # 가장 큰 수
# 가장 큰 수를 k번 더하기 -> 두 번째로 큰 수 1번 더하기 이것을 반복.
data.sort(reverse=True)
first, second = data[0], data[1] # 가장 큰 수, 두 번째로 큰 수

while True:
    for _ in range(k): # 가장 큰 수 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second # 두 번째로 큰 수 한 번 더하기
    m -= 1

print(result)