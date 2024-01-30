# 숨바꼭질
# 수빈 n, 동생 k 위치
# 1) 걷기 1초 후 x-1 / x+1 2) 순간이동) 1초 후 2*x
# 동생 찾는 최단 시간
import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
max = 10**5
distance = [0] * (max +1)
def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(distance[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max:
                if distance[i] == 0:
                    distance[i] = distance[x] + 1
                    queue.append(i)
bfs()

