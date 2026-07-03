def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 비용 기준 오름차순
    link = set([costs[0][0]]) # 시작 연결점을 set에 추가

    while len(link) != n: # 모든 섬이 연결될 때까지
        for v in costs:
            # 두 섬이 이미 낮은 가격으로 연결 -> 무시
            if v[0] in link and v[1] in link:
                continue
            # 두 섬 중 하나가 연결 X -> 비용 누적
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]]) # 연결된 섬 추가
                # set.update : 이미 섬이 연결된 경우 중복된 섬 제외 - 최대 n개 유지
                answer += v[2] # 비용 누적
                break

    return answer