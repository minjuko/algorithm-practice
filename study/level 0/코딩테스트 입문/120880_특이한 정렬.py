def solution(numlist, n):
    # 정렬 기준 > 거리 가까운 순 > 같은 경우 내림차순
    return sorted(numlist, key=lambda x: (abs(x - n), -x))