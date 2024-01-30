# 이상한 문자 만들기

# 한 개 이상 단어로 구성된 문자열
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째는 소문자로

def solution(s):
    answer = ''
    words = list(s.split(' '))

    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1]