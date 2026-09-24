# JadenCase 문자열 만들기

# 첫 문자 대문자, 나머지 소문자
# 문자열을 JadenCase로 변환하기

def solution(s):
    words = s.split(' ')
    words = [word.capitalize() for word in words]
    answer = ' '.join(words)
    return answer