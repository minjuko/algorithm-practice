"""
탐욕법 - 조이스틱
A로만 채워진 문자열 -> 목표 문자열로 변경하는 최소 조작횟수 구하기
상/하 조작 : 'A' -> 목표 알파벳으로 변경 (상:다음, 하:이전)
좌/우 조작 : 변경할 문자에 방문하는 커서 이동
전체 조작 횟수 = 모든 알파벳 변경 횟수 + 커서 이동 횟수
"""
def solution(name):
    n = len(name)
    up_down_moves = 0 # 상하 조작 횟수

    left_right_moves = n - 1 # 좌우 조작 횟수 (기본:끝까지 오른쪽으로 이동)

    for i in range(n):
        # 1. 상/하 알파벳 변경 횟수 계산
        diff = ord(name[i]) - ord('A')
        up_down_moves += min(diff, 26 - diff)

        # 2. 현재 위치 이후 연속된 'A'가 끝나는 위치 찾기
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # 3. 좌/우 커서 이동 최솟값 업데이트
        # - 기존 최솟값 (n-1)
        # - 0->i 이동 후, 왼쪽으로 돌아가 next_i 이동 = i*2 + (n-next_i)
        # - 0->next_i 이동 후, 오른족으로 돌아가 i 이동 = (n-next_i)*2 + i
        left_right_moves = min(left_right_moves, i * 2 + (n - next_i), (n - next_i) * 2 + i)
    # 상/하 + 좌/우 조작 최솟값 return
    return up_down_moves + left_right_moves