# 최댓값 연산

x, y, z = map(int, input().split())

a = max(x, y, z)
b = min(x, y, z)

if [x, y, z] == [a, b, a] or [x, y, z] == [a, a, b] or [x, y, z] == [b, a, a]:
    print("possible")
else:
    print("impossible")