# 문자열 조합하기
from itertools import combinations # 조합
A = input().rstrip()
k = int(input())

# 문자열 A에 대한 조합 C(A, k)를 오름차순으로 출력
def solution(A, k):
    comb_A = list(combinations(A, k))
    C = list(''.join(a) for a in comb_A) # 조합된 튜플들을 문자열로 변환
    C.sort() # 오름차순 정렬
    for c in C:
        print(c)
solution(A, k)
