def solution(a, b):
    answer1 = int(str(a) + str(b))
    answer2 = max(answer1, 2 * a * b)
    return answer2