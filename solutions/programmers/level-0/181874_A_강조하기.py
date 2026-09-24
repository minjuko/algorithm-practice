def solution(myString):
    answer = ""

    for char in myString:
        if char == "a" or char == "A":
            answer += "A"

        # 나머지 알파벳은 모두 소문자로 변환
        else:
            answer += char.lower()

    return answer