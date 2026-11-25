# 1이 될 때까지
# 연산: n에서 1을 뺀다 / n을 k로 나눈다
# 연산 최소 횟수 구하기

# 최대한 k로 나눈다 -> 나누어 떨어지지 않을 때 1을 뺀다
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0: # 나누어 떨어지지 않을 때 -1 연산
        n -= 1
        result += 1
    n //= k # 나누기 연산
    result += 1

while n > 1: # 남은 수에 대해 -1 연산 처리
    n -= 1
    result += 1

print(result)

