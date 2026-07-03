# 친척 수

# 친척 수 : n개 수를 m으로 나누었을 때 나머지가 모두 같게 되는 모든 m
# 가능한 모든 친척 수 구하기
from math import gcd
n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
diffs = [nums[i] - nums[i - 1] for i in range(1, n)]
diff = diffs[0]

for d in diffs[1:]:
    diff = gcd(diff, d)
    relatives = set()
    for i in range(1, int(diff ** 0.5) + 1):
        if diff % i == 0:
            relatives.add(i)
            relatives.add(diff // i)

for i in sorted(relatives):
    print(i, end=' ')



