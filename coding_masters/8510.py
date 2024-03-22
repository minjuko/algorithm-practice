# 8510 구간 단속
import sys
input = sys.stdin.readline
meter = int(input()) # 구간의 길이 (단위 m)
n = int(input()) # 로그 수

log = {}

for _ in range(n*2):
    num, time = input().split() # 차번호, 시간
    h, m, s = map(int, time.split(':')) # 시, 분, 초 분할
    time = h * 3600 + m * 60 + s # 초로 변환

    if num in log:
        log[num].append(time)
    else:
        log[num] = [time]

for i in log:
    log[i] = int(meter / ((log[i][1] - log[i][0]) / 3600))

log = sorted(log.items())
for num, speed in log:
    print(num, speed)






