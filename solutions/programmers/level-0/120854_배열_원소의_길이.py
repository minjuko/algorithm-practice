def solution(strlist):
    answer = []
    for str in strlist:
        answer.append(len(str))
    return answer
# 간단한 풀이
# answer = list(map(len, strlist))