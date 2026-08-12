def solution(x):
    # 각 자릿수 합 계산하기
    digit_sum = sum(int(digit) for digit in str(x))

    if x % digit_sum == 0:
        return True
    else:
        return False

# 다른 방법
#     digit_sum = 0
#     temp = x

#     while temp > 0:
#         digit_sum += temp % 10  # 마지막 자릿수 더하기
#         temp //= 10             # 마지막 자릿수 제거

#     return x % digit_sum == 0