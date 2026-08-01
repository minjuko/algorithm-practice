def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
               return 0
    # for문을 통과하면 조건을 만족한 것
    return 1