# 1이 될 때까지
# n이 1이 될 때까지 두 과중 하나를 반복적으로 선택하여 수행 -> 최소 횟수 구하기
# 과정 1: n에서 1을 뺸다.
# 과정 2: n을 k로 나눈다. (n이 k로 나누어떨어질 때만)

# 아이디어 : n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    # n이 k보다 작을 때 -> 더 이상 나눌 수 없음
    if n < k:
        break

    # k로 나누기
    result += 1
    n //= k

# 남은 수에서 1씩 빼기
result += (n - 1)
print(result)