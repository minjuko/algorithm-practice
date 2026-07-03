# 기둥 세우기

n, m = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]

# 세로줄에서 기둥이 있는지 확인
vertical = sum(1 for j in range(m) if all(castle[i][j] for i in range(n)))
# 가로줄에서 기둥이 있는지 확인
horizontal = sum(1 for i in range(n) if all(castle[i]))

# 가장 적은 기둥 수 출력
print(max(vertical, horizontal))
