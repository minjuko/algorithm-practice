def solution(a, b):
    # 2016년 각 월
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 금요일 기준 각 요일
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    # 1월 1일 기준 총 몇 일이 지났는지 계산 -> 7로 나눈 나머지
    # a월 이전까지 일 수 합 + b-1
    result = sum(months[:a - 1]) + (b - 1)

    # 요일 계산
    return days[result % 7]