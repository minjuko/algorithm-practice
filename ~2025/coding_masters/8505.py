# 이별 30분 전

h, m = map(int, input().split()) # 시간 분

# 현재 시각의 30분 전 시각 출력

# 분이 30분 미만일 시 시간에서 1 빼고 분에 30 더하기
if m < 30:
    m += 30
    h -= 1
    if h < 0:
        h = 23
else:
    m -= 30
print(h, m)