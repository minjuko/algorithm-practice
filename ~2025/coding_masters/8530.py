# 사탕 꺼내기

from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = deque(range(1, n + 1))

cnt = 0
for a in nums:
    if a not in q:
        continue
    idx = q.index(a)
    if idx >= len(q) - idx:
        cnt += len(q) - idx
        q.rotate(len(q) - idx)
    else:
        cnt += idx
        q.rotate(-idx)
    q.remove(a)
print(cnt)