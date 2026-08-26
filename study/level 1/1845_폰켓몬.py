def solution(nums):
    # 중복 없는 종류의 수와 n/2 중 작은 값 선택
    result = min(len(nums)//2, len(set(nums)))
    return result