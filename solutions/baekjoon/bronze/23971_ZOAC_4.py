# ZOAC 4

# 1인 테이블 W개씩 H행
# 세로로 N칸 또는 가로로 M칸 이상 비워야 함 -> 다른 참가자와 세로줄 번호 차가 N 이상 또는 가로줄 번호 차가 M 이상
# 최대 수용 인원 구하기

import math

H, W, N, M = map(int, input().split())

row = math.ceil(H/(N+1))
col = math.ceil(W/(M+1))
result = row * col
print(result)

