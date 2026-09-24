# 페인트칠하는 최소 횟수 구하기
# -> 아직 칠해지지 않은 가장 앞쪽 구역부터 롤러의 길이만큼 한 번에 칠해야함
def solution(n, m, section):
    result = 0 # 페인트칠 횟수
    now_painted = 0 # 현재 페인트가 칠해진 끝 위치

    # 1. 페인트칠해야하는 구역 순서대로 찾기
    # 2. 칠해지지 않은 구역 발견 시 해당 위치부터 m미터만큼 한 번에 덧칠 (현재위치 + m - 1)
    # 3. 롤러가 칠하는 범위를 'now-painted'에 저장 -> section의 다음 구혁이 이 범위에 포함되는지 확인
    # 4. 칠해진 범위 내 구역은 건너뛰고 범위를 벗어난 구역을 만나면 페인트칠
    for s in section:
        if s > now_painted:
            result += 1
            now_painted = s + m - 1 # 현재 위치부터 m미터만큼 칠함

    return result