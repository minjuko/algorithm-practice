def solution(strArr):
    answer = []

    for ch in strArr:
        if "ad" not in ch:
            answer.append(ch)
    return answer