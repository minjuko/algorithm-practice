# 카페 사장 철수

import heapq

def time_trans(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

n, m = map(int, input().split())

visit = [(time_trans(s), time_trans(e)) for _ in range(m) for s, e in [input().split()]]
visit.sort()

cur_cnt = 0
total = 0
heap = []

for start, end in visit:
    while heap and heap[0] <= start:
        heapq.heappop(heap)
        cur_cnt -= 1

    if cur_cnt < n:
        cur_cnt += 1
        total += 1
        heapq.heappush(heap, end)

print(total)
