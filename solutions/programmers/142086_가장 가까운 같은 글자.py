def solution(s):
    answer = [] # 각 글자 연산 결과
    last_seen = {} # 문자의 마지막 등장 위치 : 문자

    for idx, val in enumerate(s):
        # 가까운 같은 글자 위치 계산
        if val in last_seen:
            answer.append(idx-last_seen[val])
        # 처음 등장한 경우 -1
        else:
            answer.append(-1)

        last_seen[val] = idx # 마지막 등장 위치 업데이트

    return answer