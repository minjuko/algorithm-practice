def solution(sizes):
    # [긴 변, 짧은 변] 으로 통일해서 최댓값 구하기
    max_w, max_h = 0, 0

    for size in sizes:
        w, h = size

        longer, shorter = max(w, h), min(w, h)

        # 지금까지의 최댓값과 비교해서 갱신
        if longer > max_w:
            max_w = longer
        if shorter > max_h:
            max_h = shorter

    return max_w * max_h