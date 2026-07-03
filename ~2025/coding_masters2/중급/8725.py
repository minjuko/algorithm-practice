# 뮤지컬

from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = 10000
start = 0
counter = Counter()

for i in range(n):
    counter[a[i]] += 1
    while len(counter) == k:
        answer = min(answer, i - start + 1)
        counter[a[start]] -= 1

        if counter[a[start]] == 0:
            del counter[a[start]]
        start += 1

print(answer)
