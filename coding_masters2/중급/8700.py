# 좋은 배열

n = int(input())
a = list(map(int, input().split()))

goods = []

def solve(arr):
    if len(arr) % 2 != 0:
        goods.append(0)
        return
    if len(arr) == 2 or len(arr) == 0:
        goods.append(1)
        return

    s = arr[0]
    e = arr[1:].index(s)+1

    solve(arr[1:e])
    solve(arr[e+1:])

solve(a)
if 0 in goods:
    print("NO")
else:
    print("YES")
