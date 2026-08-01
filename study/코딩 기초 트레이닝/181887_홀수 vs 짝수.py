def solution(num_list):
    result1 = sum(num_list[::2])
    result2 = sum(num_list[1::2])

    return max(result1, result2)