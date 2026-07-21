def solution(chicken):
    answer = 0

    while chicken >= 10:  # 서비스가 가능할 때까지
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div + mod  # 주문한 치킨(새로 발급되는 쿠폰) 수와 남은 쿠폰 수 더하기
    return answer