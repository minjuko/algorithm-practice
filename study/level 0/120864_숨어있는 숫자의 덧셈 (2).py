def solution(my_string):
    answer = 0
    tmp = "" # 연속된 수 저장
    for ch in my_string:
        if ch.isdigit():
            tmp += ch
        # 문자 들어오면 이전에 들어온 숫자 계산
        else:
            if tmp:
                answer += int(tmp)
                tmp = ""
    # 마지막에 숫자 남아있는지 확인
    if tmp:
        answer += int(tmp)
    return answer