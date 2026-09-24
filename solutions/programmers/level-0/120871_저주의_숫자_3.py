def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        # 3의 배수 혹은 숫자 3이 포함될 때 카운트
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer