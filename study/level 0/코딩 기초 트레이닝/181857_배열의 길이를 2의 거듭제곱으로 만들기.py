def solution(arr):
    k = 1  # arr의 길이보다 크거나 같은 2의 거듭제곱 구하기
    while k < len(arr):
        k *= 2

    return arr + [0] * (k - len(arr))