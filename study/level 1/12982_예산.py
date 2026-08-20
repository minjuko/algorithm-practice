def solution(d, budget):
    # 최대한 많은 부서 -> 신청 금액이 작은 부서부터
    result = 0  # 지원한 부서 수
    d.sort()

    for i in d:
        if budget >= i:
            result += 1
            budget -= i
    return result