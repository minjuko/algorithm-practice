def solution(dots):
    # 평행 계산
    # 두 점 (x1, y1), (x2, y2)를 지나는 직선의 기울기가 같으면 평행
    # (y2-y1)/(x2-x1)
    def check(n1, n2, n3, n4):
        nx1 = n2[0] - n1[0]
        ny1 = n2[1] - n1[1]
        nx2 = n4[0] - n3[0]
        ny2 = n4[1] - n3[1]

        return nx1 * ny2 == ny1 * nx2

    if check(dots[0], dots[1], dots[2], dots[3]):
        return 1
    if check(dots[0], dots[2], dots[1], dots[3]):
        return 1
    if check(dots[0], dots[3], dots[1], dots[2]):
        return 1

    return 0