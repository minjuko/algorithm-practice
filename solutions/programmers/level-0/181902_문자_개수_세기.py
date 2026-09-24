def solution(my_string):
    answer = [0] * 52

    for ch in my_string:
        if ch.isupper():
            # 대문자 인덱스 계산
            # ex. A 0> 65 - 65 = 0 / Z 90 - 65 = 25
            index = ord(ch) - ord("A")
            # 소문자는 인덱스 26부터 저장
        else:
            index = ord(ch) - ord("a") + 26

        answer[index] += 1
    return answer