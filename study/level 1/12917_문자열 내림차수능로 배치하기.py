def solution(s):
    # ASCII 코드 기준 대문자는 소문자보다 값이 작으므로 내림차순 정렬 시 조건 충족
    return "".join(sorted(s, reverse=True))