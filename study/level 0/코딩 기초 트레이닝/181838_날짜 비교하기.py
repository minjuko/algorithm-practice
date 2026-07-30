def solution(date1, date2):
    # 연도가 앞선다
    if date1[0] < date2[0]:
        return 1
    # 연도가 같은 경우 월, 일 비교
    elif date1[0] == date2[0]:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] < date2[2]:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

    # 다른 풀이
    # return int(date1 < date2)