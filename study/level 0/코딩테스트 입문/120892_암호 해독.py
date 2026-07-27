def solution(cipher, code):
    answer = ''
    # 문자열 인덱스는 0부터 시작 -> 첫 번째 문자열은 -1 해서 생각
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer