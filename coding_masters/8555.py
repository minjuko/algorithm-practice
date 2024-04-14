# 그림 곱하기

def solve(num):
    tmp = []
    for x in range(n // num):
        tmp.append(graph[x][:m // num])

    for x in range(n):
        for y in range(0, m, m // num):
            if graph[x][y:y + m // num] != tmp[x % len(tmp)]:
                return 0
    else:
        return tmp

n, m = map(int, input().split())
graph = [input() for _ in range(n)]

area = []
for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
        area.append(i)

for num in area:
    result = solve(num)
    if result != 0:
        for i in result:
            print(i)
        break
