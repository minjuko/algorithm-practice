# 잭과 마법의 나무

from collections import deque

def solve(n):
    day = 0
    pre, cur = 1, 1
    visit = set((pre, cur))
    q = deque([(pre, cur)])

    while q:
        day += 1
        for _ in range(len(q)):
            pre, cur = q.popleft()
            # 맑음
            next = pre + cur
            if next == n:
                return day
            if (cur, next) not in visit:
                visit.add((cur, next))
                q.append((cur, next))
            # 흐림
            next = max(1, cur-1)
            if next == n:
                return day
            if (cur, next) not in visit:
                visit.add((cur, next))
                q.append((cur, next))
            # 폭풍우
            next = (pre + cur) // 2
            if next == n:
                return day
            if (cur, next) not in visit:
                visit.add((cur, next))
                q.append((cur, next))

result = []
for _ in range(int(input())):
    n = int(input())
    result.append(solve(n))

print('\n'.join(map(str, result)))
