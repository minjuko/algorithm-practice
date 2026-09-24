def solution(mats, park):
    rows, cols = len(park), len(park[0])
    mats.sort(reverse=True)  # 큰 돗자리부터 검사

    for mat in mats:
        # 돗자리의 왼쪽 위 시작 위치
        for row in range(rows - mat + 1):
            for col in range(cols - mat + 1):
                flag = True

                # mat × mat 영역 확인
                for r in range(row, row + mat):
                    for c in range(col, col + mat):
                        if park[r][c] != "-1":
                            flag = False
                            break

                    # 빈 공간이 아닌 칸을 발견하면 행 반복도 종료
                    if not flag:
                        break

                # 현재 위치에 돗자리를 놓을 수 있음
                if flag:
                    return mat

    # 어떤 돗자리도 놓을 수 없음
    return -1