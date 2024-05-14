# 기차와 파리

def fly_distance(x, y, z):
    total_distance = 0
    train1_distance = 0
    train2_distance = x

    while train1_distance != train2_distance:
        # 파리가 이동하는 거리는 두 기차 사이의 거리입니다.
        total_distance += abs(train1_distance - train2_distance)
        # 각 기차의 이동 거리를 계산합니다.
        train1_distance += y
        train2_distance -= y

        # 만약 파리가 충돌한 경우 반대 방향으로 날아갑니다.
        if train1_distance == train2_distance:
            break

        # 파리가 기차와 충돌한 경우 반대 방향으로 날아갑니다.
        total_distance += z

    return total_distance


# 입력 받기
X, Y, Z = map(int, input().split())

# 결과 출력
print(fly_distance(X, Y, Z))
