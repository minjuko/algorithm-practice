# 이웃

n, m, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

def solve():
    answer = 0
    while True:
        flag = False
        for u, v in edges:
            tmp = abs(s[u-1] - s[v-1])
            if tmp > k:
                flag = True
                cost = tmp - k
                answer += cost

                if s[u-1] < s[v-1]:
                    s[u-1] += cost
                else:
                    s[v-1] += cost
        if not flag:
            break
    return answer

print(solve())
