def solution(array):
    answer = 0
    for num in array:
        num = str(num)
        for i in num:
            if i == "7":
                answer += 1
    return answer