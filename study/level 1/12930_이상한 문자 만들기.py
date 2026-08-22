def solution(s):
    result = []

    # 공백 기준 각 단어별로 대소문자 변환
    for word in s.split(" "):
        convert_word = ""  # 변환한 단어 1개 저장
        for i in range(len(word)):
            if i % 2 == 0:
                convert_word += word[i].upper()
            else:
                convert_word += word[i].lower()
        result.append(convert_word)

    # 각 변환한 단어들을 공백을 기준으로 연결
    return " ".join(result)