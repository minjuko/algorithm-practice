def solution(num_list):
    answer = 1  # 곱 계산

    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            answer *= num

    return answer

# math.prod 사용
# import math
# return math.prod(num_list)