def solution(n, lost, reserve):

    # 1. 여벌 체육복을 가져왔는데 도난당한 학생 제외한 집합 만들기
    final_reserve = set(reserve) - set(lost)
    final_lost = set(lost) - set(reserve)

    # 2. 여벌 체육복이 있는 학생 기준 앞/뒷번호에게 빌려주기
    for i in sorted(final_reserve):
        if i-1 in final_lost:
            final_lost.remove(i-1) # 앞 번호에게 빌려주기
        elif i+1 in final_lost:
            final_lost.remove(i+1) # 뒷 번호에게 빌려주기

    # 3. 최종적으로 전체 학생 수에서 체육복이 없는 학생 제외
    return n - len(final_lost)
