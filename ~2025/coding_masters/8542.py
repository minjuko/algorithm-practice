# 도어락

import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

dict = {
    1: {2: [2, 4, 5], 3: [3, 6, 7, 8, 9]},
    2: {2: [1, 3, 4, 5, 6], 3: [7, 8, 9]},
    3: {2: [2, 6, 5], 3: [1, 4, 7, 8, 9]},
    4: {2: [1, 2, 5, 7, 8], 3: [3, 6, 9]},
    5: {2: [1, 2, 3, 4, 6, 7, 8, 9], 3: []},
    6: {2: [2, 3, 5, 8, 9], 3: [1, 4, 7]},
    7: {2: [4, 5, 8], 3: [1, 2, 3, 6, 9]},
    8: {2: [4, 5, 6, 7, 9], 3: [1, 2, 3]},
    9: {2: [5, 6, 8], 3: [1, 2, 3, 4, 7]},
}

arr = [1 for _ in range(9)]

for time in times:
    if time == 1:
        continue

    tmp = [0 for i in range(9)]
    for i in range(9):
        if arr[i] == 0: continue
        for j in dict[i + 1][time]:
            tmp[j - 1] += arr[i]
    arr = tmp

answer = sum(arr)%1000000007
print(answer)