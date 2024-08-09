# 문자열 나열하기
from itertools import permutations # 순열 구하기
A = input()


# A로 생성되는 모든 문자열 집합 P(A)를 오름차순으로 출력
def solution(A):
    P = ''.join(sorted(A)) # 문자열 A를 정렬된 배열로 변환 후 문자열로 변환
    PA = []
    for p in permutations(P):
        PA.append(''.join(p)) # 순열을 문자열로 변환 후 배열에 추가
    for pa in PA:
        print(pa)

solution(A)

