def solution(arr):
    tmp = []  # 2가 있는 인덱스 저장

    for i in range(len(arr)):
        if arr[i] == 2:
            tmp.append(i)

    if not tmp:
        return [-1]

    return arr[tmp[0]:tmp[-1] + 1]