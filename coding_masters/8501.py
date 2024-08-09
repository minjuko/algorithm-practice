# 배수 만들기
import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
nums = list(map(str, input().split()))
nums.sort(reverse=True)

for i in permutations(nums, n):
    if int(''.join(i)) % 300 == 0:
        print(''.join(i))
        exit()
print(-1)
