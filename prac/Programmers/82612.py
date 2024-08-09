#  부족한 금액 계산하기

# N번째 이용 시 이용료의 N개 받음
# count번 타게 될 시 금액이 얼마나 모자라는지 구하기

def solution(price, money, count):
    rest = 0 # 사용할 금액
    for i in range(1, count+1):
        rest += price * i
    if rest > money:
        answer = rest - money
    # 금액이 모자라지 않은 경우
    else:
        answer = 0
    return answer