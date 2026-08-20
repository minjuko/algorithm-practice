from itertools import combinations


def solution(number):
    # 학생 3명 번호 합이 0이면 삼총사
    # 삼총사를 만들 수 있는 방법의 수

    result = 0  # 방법의 수
    # 3명을 뽑는 모든 조합 탐색
    for comb in combinations(number, 3):
        if sum(comb) == 0:
            result += 1

    return result