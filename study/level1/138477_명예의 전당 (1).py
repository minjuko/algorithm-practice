import heapq

def solution(k, score):
    # 최소 힙
    # 매일 점수를 힙에 넣은 후, 힙의 크기가 k를 초과하면 가장 작은 값 제거
    # heap[0] : 최하위 점수
    result = []
    fames = []  # 명예의 전당. 최소 힙으로 관리

    for s in score:
        heapq.heappush(fames, s)  # 점수 추가
        # k개 초과 시 최하위 점수 제거
        if len(fames) > k:
            heapq.heappop(fames)
        # 최하위 점수 저장
        result.append(fames[0])

    return result