# 정수 관찰

import math
from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
M = 1000000001

result = 0
for i in range(1, n+1):
    for j in combinations(a, i):
        tmp = j[0]
        for k in j[1:]:
            tmp = tmp * k // math.gcd(tmp, k)
        if i % 2:
            result += M // tmp
        else:
            result -= M // tmp

print(result)