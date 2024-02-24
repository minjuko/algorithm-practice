# 정수를 거꾸로 출력하기

A = int(input())

# 정수의 각 자릿수를 거꾸로 출력 (낮은 자릿수부터)
# 0으로 시작은 제거

def solution(A):
    check = 0  # 가장 낮은 자리 0 체크를 위함 (0이 아닌 수가 나온 이후부터 출력)
    while A > 0:
        # 가장 낮은 자릿 수는 0이 아니어야 함  + 이전에 숫자를 출력한 적이 있어야 함
        if A % 10 != 0 or check == 1:
            print(A % 10, end='')
            check = 1
        A = A// 10

solution(A)