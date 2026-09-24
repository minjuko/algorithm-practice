def solution(n, k):
    # 양꼬치 n인분 가격 + 음료수 개수에서 서비스 개수 제외
    answer = 12000 * n + 2000 * (k - n // 10)
    return answer