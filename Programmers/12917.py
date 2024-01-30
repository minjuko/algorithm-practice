# 문자열 내림차순으로 배치하기

# 문자를 큰 것부터 작은 순으로 정렬
def solution(s):
    answer = ''
    s = list(s)  # 정렬하기 위해 배열로 변환
    s = sorted(s, reverse=True)  # 문자열 역순으로 정렬

    print(s)
    answer = ''.join(s)
    return answer