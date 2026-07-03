# K 번째 다음 순열

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n, k = map(int, input().split())
arr = list(map(int, input().split()))

fac_n = factorial(n)
k %= fac_n

for _ in range(k):
    idx = n-2
    while idx >= 0 and arr[idx] >= arr[idx+1]:
        idx -= 1

    if idx == -1:
        arr.reverse()
        continue

    idx2 = n-1
    while arr[idx] >= arr[idx2]:
        idx2 -= 1

    arr[idx], arr[idx2] = arr[idx2], arr[idx]
    arr[idx+1:] = reversed(arr[idx+1:])

print(*arr)

