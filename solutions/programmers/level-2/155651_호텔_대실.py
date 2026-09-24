import heapq


# 시간을 분단 위로 변환
# hh:mm
def time_trans(date):
    h, m = date.split(":")
    return int(h) * 60 + int(m)


def solution(book_time):
    hotel = []  # 사용 중인 객실 퇴실 시간
    q = []  # 우선순위 큐
    heapq.heapify(q)

    for s, e in book_time:
        # 예약 시간을 우선순위 큐에 저장
        s, e = time_trans(s), time_trans(e)
        heapq.heappush(q, (s, e))

    while q:
        s, e = heapq.heappop(q)  # 가장 빠른 시간 꺼내기
        # 사용 중인 객실이 없다면 객실 할당
        if not hotel:
            hotel.append(e)
        # 사용 중인 객실 중 가장 빠른 퇴실 시간(+10분 청소)보다 예약 시작 시간이 늦으면 객실 할당
        else:
            for i in range(len(hotel)):
                if hotel[i] + 10 <= s:
                    hotel[i] = e
                    break
            else:
                hotel.append(e)
    answer = len(hotel)  # 최소 객실 수
    return answer