# 정수 내림차순으로 배치하기

# n의 각 자릿수를 큰 것부터 작은 순으로 정렬

# 정수를 문자열로 바꾸어 배열에 넣고 정렬 -> 다시 문자열로 바꾼 후 숫자로 변환
def solution(n):
    arr = list(str(n))
    arr.sort(reverse=True)
    answer = int(''.join(arr))
    return answer