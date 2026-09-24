from itertools import permutations

def check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    per_numbers = set()

    for i in range(1, len(numbers)+1):
        # 각 순열의 결과를 합집합
        per_numbers |= set(map(int, map(''.join, permutations(numbers, i))))

    for num in per_numbers:
        if check(num):
            answer += 1

    return answer
