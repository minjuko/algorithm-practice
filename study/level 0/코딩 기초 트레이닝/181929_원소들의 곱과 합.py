def solution(num_list):
    result1 = 1

    for num in num_list:
        result1 *= num

    if result1 < sum(num_list) ** 2:
        return 1
    else:
        return 0