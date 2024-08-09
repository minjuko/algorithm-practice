# 이동하기

from collections import deque

n1 = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
count = 0
q = deque([(0, x1, y1, [])])

while q:
    k, x, y, visited = q.popleft()
    visited += [(x, y)]
    if (k, x, y) == (n1, x2, y2):
        count += 1
        continue
    if k > n1:
        continue

    if (not (x - 1, y) in visited):
        q += [(k + 1, x - 1, y, visited.copy())]
    if (not (x, y - 1) in visited):
        q += [(k + 1, x, y - 1, visited.copy())]
    if (not (x + 1, y) in visited):
        q += [(k + 1, x + 1, y, visited.copy())]
    if (not (x, y + 1) in visited):
        q += [(k + 1, x, y + 1, visited.copy())]

print(count)
