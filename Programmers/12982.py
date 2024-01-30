# 예산

def solution(d, budget):
    answer = 0  # 최대 부서 수
    rest = 0  # 사용한 금액
    d.sort()
    for i in d:
        if ((rest + i) <= budget):
            rest += i
            answer += 1

    return answer