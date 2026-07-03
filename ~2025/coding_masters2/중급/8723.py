# 불꽃축제

n = int(input())
a = list(map(int, input().split()))

answer, max_sum = a[0], a[0]

for i in range(1, n):
    max_sum = max(max_sum + a[i], a[i])
    answer = max(answer, max_sum)

print(answer)