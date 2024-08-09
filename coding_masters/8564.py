# 막사 정찰

n, p = map(int, input().split())
adjacent = [set() for _ in range(n * 2 + 2)]
visit = [0] * (n * 2 + 2)

for i in range(2, n * 2 + 1, 2):
    adjacent[i].add(i + 1)

for _ in range(p):
    u, v = map(int, input().split())
    adjacent[u * 2 + 1].add(v * 2)
    adjacent[v * 2 + 1].add(u * 2)

answer = 0


def dfs(u, ans):
    if u == 4:
        return True
    visit[u] = ans

    for v in adjacent[u]:
        if visit[v] == ans:
            continue
        if dfs(v, ans):
            adjacent[u].remove(v)
            adjacent[v].add(u)
            return True
    return False


while dfs(3, answer + 1):
    answer += 1

print(answer)
