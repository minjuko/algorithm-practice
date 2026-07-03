# 영양 점수

from itertools import combinations

n = int(input())
arr = list(range(n))
s = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
len_arr = len(arr)

for i in combinations(range(n), len_arr//2):
    s1 = s2 = 0
    tmp = set(range(n)) - set(i)

    for j in i:
        for k in i:
            s1 += s[arr[j]][arr[k]]
    for j in tmp:
        for k in tmp:
            s2 += s[arr[j]][arr[k]]

    answer = min(answer, abs(s1 - s2))

print(answer)