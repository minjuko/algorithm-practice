def solution(order):
    answer = 0

    for menu in order:
        if menu == "anything" or "americano" in menu:
            answer += 4500
        else:
            answer += 5000

    return answer