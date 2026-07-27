def solution(n):
    # 제곱근 연산자 **
    # ** 0.5는 실수 계산을 사용하므로 매우 큰 정수에서는 부동소수점 오차 발생
    # -> math.isqrt() 활용
    # math.isqrt(n) : n의 제곱근에서 소수점 이하를 버린 정수 값 반환
    if n ** 0.5 == int(n ** 0.5):
        return 1
    else:
        return 2