def solution(wallet, bill):
    answer = 0  # 지폐를 접은 횟수

    # bill의 작은 값이 wallet의 작은 값보다 크거나 bill의 큰 값이 wallet의 큰 값보다 큰 동안 반복
    while (min(bill) > min(wallet)) or (max(bill) > max(wallet)):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1

    return answer