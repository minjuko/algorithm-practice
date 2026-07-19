def solution(numbers, direction):
    answer = []

    # 왼쪽으로 1칸 회전
    if direction == "left":
        answer = numbers[1:] + numbers[:1]
    # 오른쪽으로 1칸 회전
    else:
        answer = numbers[-1:] + numbers[:-1]
    return answer