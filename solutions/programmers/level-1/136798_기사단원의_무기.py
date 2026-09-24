def solution(number, limit, power):
    # 1~number까지 약수의 개수 계산 -> 무기 공격력 정해 총합 계산
    result = 0 # 필요한 철의 무게

    for i in range(1, number + 1):
        # 1. 제곱근을 이용하여 약수의 개수 계산
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            # i가 n의 약수인 경우, 제곱수인 경우 +1 아니면 +2(i, n/i)
            if i % j == 0:
                if j * j == i:
                    cnt += 1
                else:
                    cnt += 2
        # 2. 제한 수치 초과 확인 후 총합 계산
        if cnt > limit:
            result += power
        else:
            result += cnt
    return result
