# 행렬의 덧셈

# 같은 행, 같은 열의 값을 더한 결과

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr2[i][j] += arr1[i][j]

    return arr2