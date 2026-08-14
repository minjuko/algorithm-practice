def solution(s):
    mid = len(s) // 2
    # 짝수 - 두글자
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    # 홀수
    else:
        return s[mid]