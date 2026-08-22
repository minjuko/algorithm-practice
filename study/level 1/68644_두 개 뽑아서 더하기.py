from itertools import combinations

def solution(numbers):
    result = set()
    cases = list(combinations(numbers, 2))
    for case in cases:
        result.add(sum(case))

    # set은 순서가 없는 자료구조이므로 .sort() 직접 호출 X
    # sorted로 정렬된 리스트로 변환하기
    return sorted(result)