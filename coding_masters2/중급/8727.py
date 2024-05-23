# 사내망 접속 기록

n, m = map(int, input().split())
k = int(input())
arr = list(map(int, input().split()))
center = [1 + m * i for i in range(n)]

result = "YES"

for x, y in zip(arr, arr[1:]):
    if x == 0 or y == 0:
        if x not in center and y not in center:
            result = "NO"
            break
    elif x % m == 1 and y not in range(x, x + m) or y % m == 1 and x not in range(y, y + m):
        result = "NO"
        break
    elif (x % m == 0 and x // m - 1 != y // m) or (y % m == 0 and y // m - 1 != x // m) or (x // m != y // m):
        result = "NO"
        break

print(result)


