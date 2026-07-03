# 하샤드 수

# 하샤드 수 : x의 자릿수 합으로 x가 나누어짐

# x가 하샤드 수인지 판별
def solution(x):
    o_x = x  # 원본 x
    sum = 0  # 자릿수 합
    while (x > 0):
        sum += x % 10
        x = x // 10

    if o_x % sum == 0:
        answer = True
    else:
        answer = False
    return answer