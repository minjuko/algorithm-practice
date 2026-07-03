# 정렬된 많은 원소 사이에서 특정 원소 찾기

n, a = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n):
    if nums[i] == a:
        print(i + 1)
        break
else:
    print(-1)