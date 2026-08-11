def solution(n):
    return list(map(int, str(n)[::-1]))
# n을 문자열로 바꾸어 뒤집음 ::-1
# 각 문자를 int형으로 변환