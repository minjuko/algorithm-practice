from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())  # 편의점 수
info = [list(map(int, input().split())) for _ in range(n)]  # 거리, 포만감
d, p = map(int, input().split())  # 포만감, 목적지 거리
info.sort(key=lambda x: x[0])  # 거리순으로 정렬

queue = PriorityQueue()
cur = answer = 0

while p and cur != d:
    cur += 1
    p -= 1

    while info:
        next_d, next_p = info[0]
        if next_d == cur:
            queue.put([-next_p, next_d])
            info.pop(0)
            if info and info[0][0] == next_d:
                continue
        break

    if d == cur:
        print(answer)
        exit()

    if not p and not queue.empty():
        satis, dist = queue.get()
        satis = -satis
        answer += 1
        p += satis

print(-1 if queue.empty() else answer)

