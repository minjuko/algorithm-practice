def solution(a, b, c, d):
    from collections import Counter

    dice = [a, b, c, d]
    counts = Counter(dice)  # 각 숫자 등장 횟수
    answer = 0

    # 1. 숫자 4개 모두 같음
    if len(counts) == 1:
        answer = 1111 * a

    # 2. 서로 다른 숫자 2개
    elif len(counts) == 2:
        nums = list(counts.items())
        (p, p_count), (q, q_count) = nums

        # 3개가 같고 1개 다름
        if p_count == 3:  # 세 숫자 값이 p
            answer = (10 * p + q) ** 2
        elif q_count == 3:  # 나머지 한 숫자가 q
            answer = (10 * q + p) ** 2

        # 2개씩 값이 같음
        else:
            answer = (p + q) * abs(p - q)

    # 3. 두 숫자가 같고 나머지 두 숫자가 다름
    elif len(counts) == 3:
        tmp = []  # p, q 저장

        for number, count in counts.items():
            if count == 1:
                tmp.append(number)
        answer = tmp[0] * tmp[1]

    # 4. 네 숫자가 모두 다름
    else:
        answer = min(dice)

    return answer