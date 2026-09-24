def solution(polynomial):
    x_term, const = 0, 0  # x항, 상수항
    answer = []

    # + 기준 항 나누기
    for term in polynomial.split(' + '):
        if 'x' in term:
            if term == "x":  # 계수가 1인 경우
                x_term += 1
            else:
                x_term += int(term[:-1])  # x를 제외한 문자열을 정수로 추가
        else:
            const += int(term)

    # 결과 저장
    if x_term == 1:
        answer.append("x")
    elif x_term > 1:
        answer.append(f"{x_term}x")
    if const > 0:
        answer.append(str(const))

    # 결과가 없는 경우 처리
    if not answer:
        return "0"
    return ' + '.join(answer)