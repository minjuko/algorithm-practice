def solution(numbers):
    # 아이디어
    # 0부터 9까지 배열을 만들고, 숫자 하나씩 돌면서 numbers에 포함되는지 검사
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    for num in arr:
        if num not in numbers:
            answer += num

    return answer