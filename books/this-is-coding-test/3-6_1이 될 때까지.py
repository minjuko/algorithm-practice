# 1이 될 때까지
# 연산: n에서 1을 뺀다 / n을 k로 나눈다
# 연산 최소 횟수 구하기

# 최대한 k로 나눈다 -> 나누어 떨어지지 않을 때 1을 뺀다
n, k = map(int, input().split())
result = 0


# 시간 효율적인 풀이
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)