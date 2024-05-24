# 창문 제작

n, a, b = map(int, input().split())

cnt = 0
glass, window = 0, 0

if (n + n * b - 1) % (a - 1) == 0:
    tmp = (n + n * b - 1) // (a - 1)
else:
    tmp = (n + n * b - 1) // (a - 1) + 1
cnt += tmp
window += (a - 1) * tmp

cnt += n
glass += n
window -= n * b

print(cnt)