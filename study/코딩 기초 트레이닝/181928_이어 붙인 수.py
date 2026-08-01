def solution(num_list):
    result1, result2 = "", ""
    for num in num_list:
        if num % 2 != 0:
            result1 += str(num)
        else:
            result2 += str(num)
    return int(result1) + int(result2)