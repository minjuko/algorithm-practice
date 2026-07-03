# 숫자 맞추기

# 시작 숫자에 +1, -1, *2 연산을 반복하여 목표숫자에 도달하는 최소 횟수 구하기

from collections import deque

n, k = map(int, input().split())
q = deque()
q.append((k, 0))  # (현재 숫자, 횟수)
visited = set()
visited.add(k)

while q:
    cur, cnt = q.popleft()

    if cur == n:
        print(cnt)
        break

    if cur * 2 <= n * 2 and cur * 2 not in visited:  # 2를 곱하는 경우
        q.append((cur * 2, cnt + 1))
        visited.add(cur * 2)

    if cur + 1 <= n and cur + 1 not in visited:  # 1을 더하는 경우
        q.append((cur + 1, cnt + 1))
        visited.add(cur + 1)

    if cur - 1 > 0 and cur - 1 not in visited:  # 1을 빼는 경우
        q.append((cur - 1, cnt + 1))
        visited.add(cur - 1)
