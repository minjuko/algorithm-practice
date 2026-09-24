def solution(my_string, num1, num2):
    my_string = list(my_string)
    tmp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = tmp
    # 동시 할당도 가능
    # my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)