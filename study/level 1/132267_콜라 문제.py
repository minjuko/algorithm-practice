def solution(a, b, n):
    # 현재 가지고 있는 빈 병 n개가 교환 가능 최소 개수(a개) 이상일 때까지 바꾸는 반복
    # 빈 병의 개수:새로 얻은 병 + 남은 빈 병

    result = 0

    # 빈 병 n이 a개 이상인 동안 반복
    while n >= a:
        new_coke = (n // a) * b  # 새로 얻은 병
        result += new_coke
        n = (n % a) + new_coke  # 현재 보유한 빈 병 수 갱신

    return result