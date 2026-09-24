def solution(myString, pat):
    answer = 0

    for i in range(0, len(myString)):
        if myString[i:i + len(pat)] == pat:
            answer += 1

    return answer