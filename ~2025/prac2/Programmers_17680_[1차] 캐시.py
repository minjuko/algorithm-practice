# [1차] 캐시
# 캐시 크기에 따른 실행시간 측정

# 캐시 교체 알고리즘은 LRU (최근 적게 사용된 것부터 교체)
# cache hit -> 1 cache miss -> 5

def solution(cacheSize, cities):
    answer = 0  # 총 실행시간
    cache = []

    for city in cities:
        city = city.lower()  # 대소문자를 구별하지 않으므로 소문자로 통일

        if cacheSize:
            # cache miss - 길이가 같으면 더이상 저장 안하고 첫 번째 값 제거
            if not city in cache:
                if cacheSize == len(cache):
                    cache.pop(0)
                cache.append(city)
                answer += 5  # 실행시간 5 갱신
            # cache hit - LRU이므로 해당 도시 삭제 후 맨 뒤에 저장
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1  # 실행시간 1 갱신
        else:
            answer += 5  # cacheSize 0인 경우 miss

    return answer