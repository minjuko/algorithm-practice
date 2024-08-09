from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    visited = set()  # 방문한 숫자 기록
    queue = deque([(x, 0)])  # (현재 숫자, 연산 횟수) 형태의 큐

    while queue:
        current, cnt = queue.popleft()

        if current == y:
            return cnt

        # 현재 숫자에 다음으로 가능한 연산을 적용하여 새로운 숫자를 생성하고 큐에 추가
        next_nums = [current + n, current * 2, current * 3]
        for num in next_nums:
            if num <= y and num not in visited:
                visited.add(num)
                queue.append((num, cnt + 1))

    return -1  # 변환할 수 없는 경우