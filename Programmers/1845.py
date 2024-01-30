# 폰켓몬

# n/2마리 고르기
# 최대한 많은 종류 포켓몬 고르기
# 같은 종류는 같은 번호
def solution(nums):
    answer = 0
    o_len = len(nums) # n
    nums = set(nums)
    if len(nums) <= (o_len//2):
        answer = len(nums)
    else:
        answer = o_len//2
    return answer

# 다른 풀이
# return min(len(ls)/2, len(set(ls)))
# def solution(nums):
#     count = len(nums) //2
#     multiple = len(set(nums))
#     answer = min(count, multiple)
#     return answer