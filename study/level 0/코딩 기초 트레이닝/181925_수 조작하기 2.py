def solution(numLog):
    answer = ''
    dic = {1: "w", -1: "s", 10: "d", -10: "a"}

    for i in range(len(numLog) - 1):
        tmp = numLog[i + 1] - numLog[i]  # 인접한 원소 차를 구해 조작한 값 계산
        answer += dic[tmp]
    return answer