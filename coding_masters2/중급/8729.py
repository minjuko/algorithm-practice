# Trailing Zero - 2

n = int(input())

def trailing_zero(n):
    k, cnt = 5, 0
    while k <= n:
        cnt += n // k
        k *= 5
    return cnt

left, right = 0, n*5
while left <= right:
    mid = (left + right) // 2
    if trailing_zero(mid) < n:
        left = mid + 1
    else:
        right = mid - 1

print(left)