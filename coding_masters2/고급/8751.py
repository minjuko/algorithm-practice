import numpy as np

n = int(input())
k = int(input())
m = int(input())

road = np.array([[0]*n for _ in range(n)])
for _ in range(m):
    x, y, z, w = map(int, input().split())
    road[x-1:z, y-1:w] += 1

answer = np.sum(road//k)
print(answer)