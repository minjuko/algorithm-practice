def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)

    # 간단하게
    # answer = [money // 5500, money % 5500]
    return answer