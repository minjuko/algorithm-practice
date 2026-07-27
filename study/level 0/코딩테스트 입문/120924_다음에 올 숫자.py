# 120924 다음에 올 숫자
def solution(common):
    answer = 0
    a, b, c = common[:3]

    # 등차
    if (b - a) == (c - b):
        answer = common[-1] + (b - a)
    # 등비
    else:
        answer = common[-1] * (b // a)
    return answer