# 왕실의 나이트
# 8X8 좌표 평면, L자 형태로 이동(수평 두칸->수직 한칸 또는 수직 두칸 -> 수평 한칸)
# 행:1~8, 열:a~h
# 나이트가 이동할 수 있는 경우의 수 구하기

input_data = input() # 현재 위치 입력 (ex a1)
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1
result = 0

# 이동 가능한 방향 정의 (8개)
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 각 방향으로 이동 가능한지 확인
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    # 범위 충족하는지 확인
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)