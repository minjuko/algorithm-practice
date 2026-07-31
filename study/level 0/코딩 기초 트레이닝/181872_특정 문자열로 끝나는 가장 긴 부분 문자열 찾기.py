def solution(myString, pat):
    last_idx = 0

    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i + len(pat)] == pat:
            last_idx = i + len(pat)

    return myString[:last_idx]

    # rfind()
    # last_idx = myString.rfind(pat) + len(pat)
    # return myString[:last_idx]