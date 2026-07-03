# 야근 지수

import heapq


def solution(n, works):

    # 주어진 시간이 남은 일의 총합 이상이면 야근 필요 X
    if n >= sum(works):
        return 0 # 야근 피로도 0 반환

    works = [-w for w in works] # 최대힙 구성을 위해 음수 변환
    heapq.heapify(works) # works 리스트를 최대힙으로

    for _ in range(n): # n시간 동안
        tmp = heapq.heappop(works) # 가장 큰 작업량 꺼내기
        tmp += 1 # 해당 작업량 1 감소
        heapq.heappush(works, tmp) # 감소한 작업량 다시 최대힙에 추가
    answer = sum([w ** 2 for w in works]) # 야근 피로도 계산
    return answer