def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])  # 연산 왼쪽 숫자 저장

    for i in range(1, len(my_string), 2):
        operator = my_string[i]  # 연산자
        number = int(my_string[i + 1])  # 연산자 오른쪽 숫자

        if operator == "+":
            answer += number
        else:
            answer -= number
    return answer