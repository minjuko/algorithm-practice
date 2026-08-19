def solution(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)

    return result
# 다른 풀이
# return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
# zip(arr1, arr2) : 두 행렬에서 같은 위치의 행(a, b)를 짝지어 가져오기
# zip(a, b) : 가져온 두 행(a, b)에서 같은 위치의 원소(c, d)를 짝지어 가져오기
# c+d : 각 위치의 원소를 더하여 새 행렬 생성