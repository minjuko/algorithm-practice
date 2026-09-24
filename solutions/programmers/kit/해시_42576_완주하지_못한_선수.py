# 한 명 제외 모든 선수가 완주 -> 해당 선수 이름 찾기
from collections import Counter
def solution(participant, completion):
    # 참여자 - 완주자 차집합 계산
    answer = Counter(participant) - Counter(completion)
    # 남은 한 명의 이름 반환
    return list(answer.keys())[0]