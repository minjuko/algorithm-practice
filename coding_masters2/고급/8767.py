# 탁구 복식 경기

import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
skills = list(map(int, input().split()))
result = float('inf')

for a, b in combinations(range(n), 2):
    left = skills[a] * skills[b]
    for c, d in combinations([i for i in range(n) if i != a and i != b], 2):
        right = skills[c] * skills[d]
        result = min(result, abs(left - right))

print(result)
