def solution(intStrs, k, s, l):
    answer = []
    for ch in intStrs:
        tmp = ch[s:s+l]
        if int(tmp) > k:
            answer.append(int(tmp))
    return answer