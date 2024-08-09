# [1차] 캐시

# db 캐시 적용 시 캐시 크기에 따른 실행 시간 측정
# 도시이름 배열을 순서대로 처리하여 총 실행 시간 출력
# 캐시 교체 알고리즘 LRU 사용 (최근 적게 사용된 것부터 교체) -> 큐 형태
# cache hit -> 1 cache miss -> 5

def solution(cacheSize, cities):
    cache = []
    answer = 0 # 총 실행시간
    for city in cities:
        city = city.lower() # 대소문자 구별 X
        if cacheSize: # 캐시 사이즈 존재하는 경우 hit/miss 판별
            # miss이면 길이를 확인
            # -> 길이가 같으면 더 이상 저장 X -> 첫 번째 값 제거
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                answer += 5
            # hit이면 가장 최근 참조이므로 삭제한 뒤 맨 뒤에 다시 저장
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
        else: # 캐시 사이즈 0인 경우 cache miss
            answer += 5
    return answer