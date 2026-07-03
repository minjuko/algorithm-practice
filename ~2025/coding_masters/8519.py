# 태국 택시

n, m = map(int, input().split()) # 마을 수, 택시 수
info = [list(map(int, input().split())) for _ in range(m)] # 도시 a, 도시 b, 에약비용 c

# union-find 정의
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n + 1)] # 부모 정의
info.sort(key=lambda x: x[2]) # 비용 순으로 정렬
answer = 0

for i in info:
    a, b, cost = i
    # 사이클 발생 X 간선 추가
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost
print(answer)
