# JadenCase 문자열 만들기

# 첫 문자만 대문자

def solution(s):
    s = s.lower()
    words = s.split(' ')
    words = [word.capitalize() for word in words]

    return ' '.join(words)