# 배수 만들기

from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True) # 내림차순

# 이어붙여 만들 수 있는 가장 큰 300의 배수 구하기
for p in permutations(nums, n):
    num = int(''.join(map(str, p)))
    if num % 30 == 0:
        print(num)
        break
else:
    print(-1)


