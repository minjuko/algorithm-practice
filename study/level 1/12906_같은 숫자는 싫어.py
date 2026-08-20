def solution(arr):
    result = []
    # arr의 원소가 result의 마지막 값과 다르거나, result가 비어있을 때만 우너소 추가

    for num in arr:
        # 비어있을 때는 그냥 추가
        if not result:
            result.append(num)
        # 현재 원소와 result의 마지막 원소 비교
        else:
            if result[-1] != num:
                result.append(num)
    return result