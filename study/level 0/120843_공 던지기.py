def solution(numbers, k):
    # k번째 : 2x(k-1) 를 배열 길이로 나눈 나머지 인덱스의 값
    answer = numbers[(2 * (k - 1)) % len(numbers)]
    return answer