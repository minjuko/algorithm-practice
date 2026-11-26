# 음료수 얼려먹기
# dfs/bfs

# nxm 크기 얼음틀. 0:구멍이 뚫려 있는 부분 1:칸막이가 존재하는 부분
# 뚫려 있는 부분에서 상하좌우 붙어있는 경우 서로 연결된 것.
# 총 아이스크림 개수 구하기 (연결된 것이 몇 개인지)

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 구현 - 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y):
    # 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드 방문 여부 확인 -> 방문 안했으면 상하좌우 검사
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        # 상하좌우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 작업 수행
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)