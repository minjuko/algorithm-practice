def solution(price, money, count):
    # 각 횟수마다 가격 계산해서 money에서 차감
    for i in range(1, count + 1):
        money -= i * price

    # 돈이 부족하면 절댓값 씌워서 return
    return abs(money) if money < 0 else 0

    # 다른 풀이
    # 1부터 count까지의 합을 이용해 총 필요한 금액 계산
    # total_cost = price * count * (count + 1) // 2

    # 부족한 금액 계산 (남는 경우 0 반환)
    # return max(0, total_cost - money)