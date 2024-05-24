# 전자 시계

h, m = map(int, input().split(":"))
k = int(input())

saw_time = set()
cnt = 0

while True:
    format_time = f"{h:02d}:{m:02d}"
    if format_time in saw_time:
        break
    saw_time.add(format_time)
    if format(h, '02')[::-1] == format(m, '02'):
        cnt += 1
    m += k
    h += m // 60
    m %= 60
    h %= 24

print(cnt)