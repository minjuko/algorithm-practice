def solution(arr):
    # 1. 행이 더 많으면 각 행에 부족한 열만큼 0 추가
    # 2. 열이 더 많으면 부족한 행만큼 [0, 0, ...] 추가
    # 3. 같으면 그대로 반환

    row_cnt, col_cnt = len(arr), len(arr[0])

    if row_cnt > col_cnt:
        diff = row_cnt - col_cnt

        for row in arr:
            row.extend([0] * diff)
    elif col_cnt > row_cnt:
        diff = col_cnt - row_cnt

        for _ in range(diff):
            arr.append([0] * col_cnt)

    return arr
