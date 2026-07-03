# 몇 번씩 나올까

n = int(input())

# 0부터 9까지 숫자 각각 횟수 구하기

nums = [0] * 10
for i in range(1, n+1):
    for i in str(i):
        nums[int(i)] += 1
print(*nums)