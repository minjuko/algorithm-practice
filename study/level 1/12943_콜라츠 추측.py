def solution(num):
    cnt = 0

    # 수가 1이 아니고 반복 횟수 500회 미만일 동안 반복
    while num != 1 and cnt < 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        # 연산 후 카운트 갱신
        cnt += 1

    return cnt if num == 1 else -1

