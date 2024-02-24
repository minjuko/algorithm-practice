# 제일 작은 수 제거하기

# 배열에서 가장 작은 수 제거한 배열 구하기
def solution(arr):
    answer = []
    arr.remove(min(arr))
    if arr:
        return arr
    else:
        return [-1]
    return answer