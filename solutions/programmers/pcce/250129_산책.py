# N, S, E, W 방향 1씩 이동
# 남쪽으로 1 = 북쪽으로 -1
# 서쪽으로 1 = 동쪽으로 -1
def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S":
            north -= 1
        elif i == "E":
            east += 1
        elif i == "W":
            east -= 1
    return [east, north]