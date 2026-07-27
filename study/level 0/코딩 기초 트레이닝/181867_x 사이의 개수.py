def solution(myString):
    answer = []
    myString = myString.split("x")
    for ch in myString:
        answer.append(len(ch))

    return answer