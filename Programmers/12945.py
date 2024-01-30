# 피보나치 수

# n번째 피보나치 수를 1234567로 나눈 나머지를 반환하기
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) (n >= 2)

def solution(n):
    answer = 0
    fibo_arr = [0, 1]
    for i in range(2, n+1):
        fibo_arr.append(fibo_arr[i-1] + fibo_arr[i-2])
    answer = fibo_arr[n] % 1234567
    return answer

