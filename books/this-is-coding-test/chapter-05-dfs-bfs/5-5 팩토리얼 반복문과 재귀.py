# 팩토리얼 구현 예제
# 1. 반복문 이용
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 2. 재귀 이용
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

# 출력해보기
print(factorial_iterative(5))
print(factorial_recursive(5))