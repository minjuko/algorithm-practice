def solution(number):
    sum_num = 0 # 각 자리 숫자 합
    for num in number:
        sum_num += int(num)
    return sum_num % 9