# 야바위

n, k = map(int, input().split())
dir = [i for i in range(n+1)]

for _ in range(0, k):
    a, b = map(int, input().split())
    dir[a], dir[b] = dir[b], dir[a]

print(dir.index(int(input())))