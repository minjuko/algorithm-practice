# 다음 큰 숫자

# 조건1. n의 다음 큰 숫자는 n보다 큰 자연수
# 조건2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 개수가 같다
# 조건3. n의 다음 큰 숫자는 조건1, 2를 만족하는 수 중 가장 작은 수

def solution(n):
    answer = 0
    n_bin = bin(n).count("1") # n의 2진수 변환 후 1의 개수

    # for num in range(n+1, 1000001):
    #     num_bin = bin(num).count("1") # num의 2진수 변환 후 1의 개수
    #
    #     if n_bin == num_bin:
    #         answer = num
    #         break

    while True:
        n = n+1
        if n_bin == bin(n).count("1"):
            answer = n
            break
    return answer

