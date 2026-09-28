def solution(s):
    answer = 0  # 분해한 문자열의 개수
    cnt1, cnt2 = 0, 0  # x, x가 아닌 수 등장 횟수

    for i in s:
        if cnt1 == cnt2:
            answer += 1
            start = i
        if i == start:
            cnt1 += 1
        else:
            cnt2 += 1

    return answer