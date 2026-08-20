def solution(t, p):
    count = 0

    # for문 범위 설정
    # 길이가 len(p)인 부분 문자열이 만들어질 수 있는 마지막 시작 인덱스까지
    # 마지막 시작 인덱스 : len(t) - len(p)
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            count += 1

    return count