# 8689 선물

import math
from functools import reduce

n = int(input()) # 선물 종류 수
a = list(map(int, input().split())) # 각 종류 선물 개수

answer = reduce(math.gcd, a) # 선물 받게 되는 최대 명수

print(answer)
