def solution(myString, pat):
    answer = ""

    for ch in myString:
        if ch == "A":
            answer += "B"
        else:
            answer += "A"

    if pat in answer:
        return 1
    else:
        return 0