def solution(food):
    # 음식 대칭 배치, 중앙에는 물(0)
    # 각 음식 수량을 2로 나눈 몫만큼 한쪽 선수 + 중앙에 물 + 오른쪽에 뒤집어서 배치

    left = ""
    for i in range(1, len(food)):
        left += str(i) * (food[i] // 2)

    return left + "0" + left[::-1]